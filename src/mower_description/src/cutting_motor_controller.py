#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from mower_description.srv import CuttingMotorControl
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class CuttingMotorController(Node):
    def __init__(self):
        super().__init__('cutting_motor_controller')
        
        # 速度档位映射
        self.speed_levels = {
            0: 0.0,    # 关闭
            1: 20.0,   # 一档
            2: 40.0,   # 二档
            3: 60.0    # 三档
        }

        self.current_speed = 0.0
        self.current_position = 0.0
        self.command_period = 0.05  # 20 Hz trajectory update
        self.last_update_time = self.get_clock().now()

        # 创建状态发布者
        self.status_publisher = self.create_publisher(
            String, 
            '/mower/cutting_motor/status', 
            10
        )

        # 使用 joint pose trajectory 插件的命令 topic
        self.traj_publisher = self.create_publisher(
            JointTrajectory,
            '/mower/blade/set_joint_trajectory',
            10
        )
        
        # 创建服务
        self.service = self.create_service(
            CuttingMotorControl, 
            '/mower/cutting_motor/control', 
            self.control_callback
        )

        self.timer = self.create_timer(self.command_period, self.publish_blade_trajectory)
        self.get_logger().info('Cutting motor controller started')

    def publish_blade_trajectory(self):
        now = self.get_clock().now()
        dt = (now - self.last_update_time).nanoseconds / 1e9
        # 防止仿真时间回跳或暂停导致积分异常
        if dt < 0.0:
            dt = 0.0
        if dt > 0.2:
            dt = 0.2
        self.last_update_time = now

        # 将速度命令积分成位置命令，兼容 gazebo_ros_joint_pose_trajectory 插件
        self.current_position += self.current_speed * dt

        traj = JointTrajectory()
        traj.header.stamp = now.to_msg()
        traj.header.frame_id = 'base_link'
        traj.joint_names = ['blade_joint']

        point = JointTrajectoryPoint()
        point.positions = [self.current_position]
        point.velocities = [self.current_speed]
        # 轨迹时长与发布周期一致，避免控制器丢点
        point.time_from_start = Duration(
            sec=0, nanosec=int(self.command_period * 1e9)
        )
        traj.points = [point]

        self.traj_publisher.publish(traj)

    def control_callback(self, request, response):
        speed_level = request.speed_level

        if speed_level not in self.speed_levels:
            response.success = False
            response.message = f'Invalid speed level: {speed_level}. Valid levels are 0-3.'
            response.actual_speed = 0.0
            return response

        # 获取对应档位的速度
        speed = self.speed_levels[speed_level]

        # 更新旋转速度（由定时器持续发布轨迹）
        self.current_speed = speed
        # 速度切换时对积分基准对齐，避免突变
        self.last_update_time = self.get_clock().now()

        # 发布状态消息
        status_msg = String()
        status_msg.data = str(speed_level)
        self.status_publisher.publish(status_msg)

        # 构建响应
        response.success = True
        response.message = f'Successfully set cutting motor to level {speed_level} ({speed} rad/s)'
        response.actual_speed = speed

        self.get_logger().info(f'Cutting motor set to level {speed_level}, speed: {speed} rad/s')

        return response

def main(args=None):
    rclpy.init(args=args)
    cutting_motor_controller = CuttingMotorController()
    rclpy.spin(cutting_motor_controller)
    cutting_motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
