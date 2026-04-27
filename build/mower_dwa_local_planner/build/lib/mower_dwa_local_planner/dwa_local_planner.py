# -*- coding: utf-8 -*-
"""
DWA (Dynamic Window Approach) 局部规划器
基于动态窗口方法的机器人局部路径规划算法
"""

import math
from typing import List, Optional, Sequence, Tuple

import rclpy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Twist
from nav_msgs.msg import Odometry, Path
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


def clamp(value: float, lower: float, upper: float) -> float:
    """
    限制数值在指定范围内
    
    Args:
        value: 输入数值
        lower: 下限
        upper: 上限
        
    Returns:
        限制后的数值
    """
    return max(lower, min(upper, value))


def yaw_from_quaternion(x: float, y: float, z: float, w: float) -> float:
    """
    从四元数中提取偏航角(yaw)
    
    Args:
        x, y, z, w: 四元数的四个分量
        
    Returns:
        偏航角(弧度)
    """
    siny_cosp = 2.0 * (w * z + x * y)
    cosy_cosp = 1.0 - 2.0 * (y * y + z * z)
    return math.atan2(siny_cosp, cosy_cosp)


class DwaLocalPlanner(Node):
    """
    DWA局部规划器主类
    实现基于动态窗口方法的局部路径规划算法
    """
    
    def __init__(self) -> None:
        """初始化DWA规划器，声明所有ROS参数"""
        super().__init__('dwa_local_planner')

        # 目标朝向控制参数
        self.declare_parameter('goal_yaw_tolerance', 0.15)  # 目标朝向容差(弧度)
        self.declare_parameter('final_rotate_kp', 0.8)  # 最终旋转比例系数
        self.declare_parameter('final_rotate_max_yaw_rate', 0.5)  # 最终旋转最大角速度(rad/s)
        self.declare_parameter('final_rotate_min_yaw_rate', 0.08)  # 最终旋转最小角速度(rad/s)
        
        # 朝向目标旋转参数
        self.declare_parameter('rotate_to_goal_enter_angle', 1.75)  # 进入旋转模式的角度阈值(弧度)
        self.declare_parameter('rotate_to_goal_exit_angle', 0.35)  # 退出旋转模式的角度阈值(弧度)
        self.declare_parameter('rotate_kp', 0.8)  # 旋转比例系数
        self.declare_parameter('rotate_max_yaw_rate', 0.6)  # 旋转最大角速度(rad/s)
        self.declare_parameter('rotate_min_yaw_rate', 0.12)  # 旋转最小角速度(rad/s)
        self.declare_parameter('rotate_angle_deadband', 0.08)  # 旋转角度死区(弧度)
        
        # ROS话题参数
        self.declare_parameter('scan_topic', '/scan')  # 激光雷达话题
        self.declare_parameter('odom_topic', '/odom')  # 里程计话题
        self.declare_parameter('cmd_vel_topic', '/cmd_vel')  # 控制指令话题
        self.declare_parameter('goal_topic', '/goal_pose')  # 目标位置话题
        self.declare_parameter('path_topic', '/dwa/best_path')  # 规划路径话题
        self.declare_parameter('goal_frame', 'odom')  # 目标坐标系
        
        # 目标参数
        self.declare_parameter('use_static_goal', False)  # 是否使用静态目标
        self.declare_parameter('static_goal_x', 3.0)  # 静态目标X坐标
        self.declare_parameter('static_goal_y', 0.0)  # 静态目标Y坐标
        self.declare_parameter('goal_tolerance', 0.35)  # 目标到达容差(米)
        
        # DWA算法参数
        self.declare_parameter('control_rate', 10.0)  # 控制频率(Hz)
        self.declare_parameter('predict_time', 2.5)  # 轨迹预测时间(秒)
        self.declare_parameter('sim_dt', 0.1)  # 仿真时间步长(秒)
        self.declare_parameter('v_samples', 8)  # 线速度采样数
        self.declare_parameter('w_samples', 17)  # 角速度采样数
        
        # 机器人运动限制
        self.declare_parameter('min_speed', 0.0)  # 最小线速度(m/s)
        self.declare_parameter('max_speed', 0.7)  # 最大线速度(m/s)
        self.declare_parameter('max_yaw_rate', 1.4)  # 最大角速度(rad/s)
        self.declare_parameter('max_accel', 0.7)  # 最大线加速度(m/s²)
        self.declare_parameter('max_yaw_accel', 2.2)  # 最大角加速度(rad/s²)
        
        # 障碍物检测参数
        self.declare_parameter('robot_radius', 0.38)  # 机器人半径(米)
        self.declare_parameter('safety_margin', 0.12)  # 安全边界(米)
        self.declare_parameter('clearance_cap', 2.5)  # 最大安全距离(米)
        self.declare_parameter('obstacle_range', 6.0)  # 障碍物检测范围(米)
        
        # 轨迹评分权重
        self.declare_parameter('heading_weight', 0.52)  # 朝向权重
        self.declare_parameter('clearance_weight', 0.30)  # 安全距离权重
        self.declare_parameter('velocity_weight', 0.18)  # 速度权重
        
        # 避障旋转参数
        self.declare_parameter('escape_yaw_rate', 0.6)  # 避障旋转角速度(rad/s)
        self.declare_parameter('front_sector_half_angle', 0.55)  # 前方扇形区域半角(弧度)
        self.declare_parameter('front_sector_range', 1.5)  # 前方扇形区域范围(米)

        # 获取并设置所有参数值
        self.goal_yaw_tolerance = float(self.get_parameter('goal_yaw_tolerance').value)  # 目标朝向容差
        self.final_rotate_kp = float(self.get_parameter('final_rotate_kp').value)  # 最终旋转比例系数
        self.final_rotate_max_yaw_rate = float(self.get_parameter('final_rotate_max_yaw_rate').value)  # 最终旋转最大角速度
        self.final_rotate_min_yaw_rate = float(self.get_parameter('final_rotate_min_yaw_rate').value)  # 最终旋转最小角速度
        self.rotate_to_goal_enter_angle = float(self.get_parameter('rotate_to_goal_enter_angle').value)  # 进入旋转角度阈值
        self.rotate_to_goal_exit_angle = float(self.get_parameter('rotate_to_goal_exit_angle').value)  # 退出旋转角度阈值
        self.rotate_kp = float(self.get_parameter('rotate_kp').value)  # 旋转比例系数
        self.rotate_max_yaw_rate = float(self.get_parameter('rotate_max_yaw_rate').value)  # 旋转最大角速度
        self.rotate_min_yaw_rate = float(self.get_parameter('rotate_min_yaw_rate').value)  # 旋转最小角速度
        self.rotate_angle_deadband = float(self.get_parameter('rotate_angle_deadband').value)  # 旋转角度死区
        
        # ROS话题配置
        self.scan_topic = self.get_parameter('scan_topic').value  # 激光雷达话题
        self.odom_topic = self.get_parameter('odom_topic').value  # 里程计话题
        self.cmd_vel_topic = self.get_parameter('cmd_vel_topic').value  # 控制指令话题
        self.goal_topic = self.get_parameter('goal_topic').value  # 目标位置话题
        self.path_topic = self.get_parameter('path_topic').value  # 规划路径话题
        self.goal_frame = self.get_parameter('goal_frame').value  # 目标坐标系
        
        # 目标配置
        self.use_static_goal = bool(self.get_parameter('use_static_goal').value)  # 是否使用静态目标
        self.static_goal_x = float(self.get_parameter('static_goal_x').value)  # 静态目标X坐标
        self.static_goal_y = float(self.get_parameter('static_goal_y').value)  # 静态目标Y坐标
        self.goal_tolerance = float(self.get_parameter('goal_tolerance').value)  # 目标到达容差
        
        # DWA算法参数
        self.control_rate = float(self.get_parameter('control_rate').value)  # 控制频率
        self.predict_time = float(self.get_parameter('predict_time').value)  # 轨迹预测时间
        self.sim_dt = float(self.get_parameter('sim_dt').value)  # 仿真时间步长
        self.v_samples = max(2, int(self.get_parameter('v_samples').value))  # 线速度采样数(至少2个)
        self.w_samples = max(3, int(self.get_parameter('w_samples').value))  # 角速度采样数(至少3个)
        
        # 运动限制参数
        self.min_speed = float(self.get_parameter('min_speed').value)  # 最小线速度
        self.max_speed = float(self.get_parameter('max_speed').value)  # 最大线速度
        self.max_yaw_rate = float(self.get_parameter('max_yaw_rate').value)  # 最大角速度
        self.max_accel = float(self.get_parameter('max_accel').value)  # 最大线加速度
        self.max_yaw_accel = float(self.get_parameter('max_yaw_accel').value)  # 最大角加速度
        
        # 障碍物检测参数
        self.robot_radius = float(self.get_parameter('robot_radius').value)  # 机器人半径
        self.safety_margin = float(self.get_parameter('safety_margin').value)  # 安全边界
        self.clearance_cap = float(self.get_parameter('clearance_cap').value)  # 最大安全距离
        self.obstacle_range = float(self.get_parameter('obstacle_range').value)  # 障碍物检测范围
        
        # 轨迹评分权重
        self.heading_weight = float(self.get_parameter('heading_weight').value)  # 朝向权重
        self.clearance_weight = float(self.get_parameter('clearance_weight').value)  # 安全距离权重
        self.velocity_weight = float(self.get_parameter('velocity_weight').value)  # 速度权重
        
        # 避障参数
        self.escape_yaw_rate = float(self.get_parameter('escape_yaw_rate').value)  # 避障旋转角速度
        self.front_sector_half_angle = float(self.get_parameter('front_sector_half_angle').value)  # 前方扇形区域半角
        self.front_sector_range = float(self.get_parameter('front_sector_range').value)  # 前方扇形区域范围

        # 状态变量初始化
        self.current_pose: Optional[Tuple[float, float, float]] = None  # 当前位姿(x, y, yaw)
        self.current_velocity: Tuple[float, float] = (0.0, 0.0)  # 当前速度(线速度, 角速度)
        self.goal_xy: Optional[Tuple[float, float]] = None  # 目标位置(x, y)
        self.goal_yaw: Optional[float] = None  # 目标朝向
        self.goal_source = 'static' if self.use_static_goal else 'unset'  # 目标来源
        self.obstacle_points: List[Tuple[float, float]] = []  # 障碍物点云
        self.latest_scan: Optional[LaserScan] = None  # 最新激光数据
        self.last_control_dt = 1.0 / self.control_rate  # 上次控制周期
        self.last_loop_time = self.get_clock().now()  # 上次循环时间
        self.reported_waiting = False  # 是否已报告等待状态
        self.last_no_goal_log_sec = -1.0  # 上次无目标日志时间
        self.last_escape_log_sec = -1.0  # 上次避障日志时间
        self.last_goal_reached_log_sec = -1.0  # 上次到达目标日志时间
        self.last_invalid_goal_log_sec = -1.0  # 上次无效目标日志时间
        self.rotating_to_goal = False  # 是否正在朝向目标旋转

        # 创建ROS发布器
        self.cmd_pub = self.create_publisher(Twist, self.cmd_vel_topic, 10)  # 控制指令发布器
        self.path_pub = self.create_publisher(Path, self.path_topic, 10)  # 规划路径发布器
        self.goal_echo_pub = self.create_publisher(PoseWithCovarianceStamped, '/dwa/goal_echo', 10)  # 目标回显发布器

        # 创建ROS订阅器
        self.create_subscription(LaserScan, self.scan_topic, self.scan_callback, 10)  # 激光数据订阅
        self.create_subscription(Odometry, self.odom_topic, self.odom_callback, 10)  # 里程计数据订阅
        self.create_subscription(PoseStamped, self.goal_topic, self.goal_callback, 10)  # 目标位置订阅
        
        # 创建控制定时器
        self.timer = self.create_timer(1.0 / self.control_rate, self.control_loop)  # 控制循环定时器

        # 启动日志
        self.get_logger().info(
            f'DWA local planner started: scan={self.scan_topic}, odom={self.odom_topic}, '
            f'cmd_vel={self.cmd_vel_topic}, goal={self.goal_topic}'
        )

    def goal_callback(self, msg: PoseStamped) -> None:
        """
        目标位置回调函数
        处理从RViz或其他节点发送的目标位置
        
        Args:
            msg: 目标位姿消息
        """
        # 检查坐标系
        frame_id = msg.header.frame_id or self.goal_frame
        if frame_id != self.goal_frame:
            self.log_periodic(
                'warn',
                f'Ignore goal in frame "{frame_id}". Expected "{self.goal_frame}".',
                'last_invalid_goal_log_sec',
                2.0,
            )
            return

        # 更新目标状态
        self.goal_xy = (msg.pose.position.x, msg.pose.position.y)  # 目标位置
        self.goal_yaw = yaw_from_quaternion(
            msg.pose.orientation.x,
            msg.pose.orientation.y,
            msg.pose.orientation.z,
            msg.pose.orientation.w
        )  # 目标朝向
        self.goal_source = 'topic'  # 标记目标来源为话题

        # 发布目标回显消息
        echo = PoseWithCovarianceStamped()
        echo.header = msg.header
        echo.pose.pose = msg.pose
        self.goal_echo_pub.publish(echo)

        # 记录目标接收日志
        self.get_logger().info(
            f'Received goal ({self.goal_xy[0]:.2f}, {self.goal_xy[1]:.2f}) in {frame_id}'
        )

    def odom_callback(self, msg: Odometry) -> None:
        """
        里程计回调函数
        更新机器人当前位姿和速度信息
        
        Args:
            msg: 里程计消息
        """
        pose = msg.pose.pose  # 位姿信息
        twist = msg.twist.twist  # 速度信息
        
        # 从四元数提取偏航角
        yaw = yaw_from_quaternion(
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w,
        )
        
        # 更新当前状态
        self.current_pose = (pose.position.x, pose.position.y, yaw)  # 当前位置和朝向
        self.current_velocity = (twist.linear.x, twist.angular.z)  # 当前线速度和角速度

    def scan_callback(self, msg: LaserScan) -> None:
        """
        激光雷达回调函数
        处理激光数据并转换为障碍物点云
        
        Args:
            msg: 激光扫描消息
        """
        self.latest_scan = msg  # 保存最新激光数据
        points: List[Tuple[float, float]] = []  # 障碍物点云列表
        angle = msg.angle_min  # 起始角度
        
        # 遍历所有激光点
        for distance in msg.ranges:
            # 检查距离是否有效且在检测范围内
            if math.isfinite(distance) and msg.range_min < distance < min(msg.range_max, self.obstacle_range):
                # 将极坐标转换为笛卡尔坐标
                points.append((distance * math.cos(angle), distance * math.sin(angle)))
            angle += msg.angle_increment  # 递增角度
        
        self.obstacle_points = points  # 更新障碍物点云

    def control_loop(self) -> None:
        """
        主控制循环
        执行DWA算法并发布控制指令
        """
        now = self.get_clock().now()
        dt = (now - self.last_loop_time).nanoseconds / 1e9
        self.last_loop_time = now
        if dt > 1e-4:
            self.last_control_dt = dt

        # 检查数据是否就绪
        if self.current_pose is None or self.latest_scan is None:
            if not self.reported_waiting:
                self.get_logger().info('Waiting for odom and scan data...')
                self.reported_waiting = True
            return

        self.reported_waiting = False
        goal = self.get_active_goal()  # 获取当前目标
        if goal is None:
            self.publish_stop()  # 停止运动
            self.publish_path([])  # 清空路径
            self.log_periodic(
                'info',
                'No active goal. Send RViz 2D Goal Pose to /goal_pose or enable use_static_goal.',
                'last_no_goal_log_sec',
                5.0,
            )
            return

        # 计算到目标的距离和方向
        x, y, yaw = self.current_pose
        goal_dx = goal[0] - x
        goal_dy = goal[1] - y
        goal_distance = math.hypot(goal_dx, goal_dy)
        
        # 检查是否到达目标
        if goal_distance <= self.goal_tolerance:
            self.publish_path([])  # 清空路径

            # 如果指定了目标朝向，进行最终旋转
            if self.goal_yaw is not None:
                yaw_error = math.atan2(
                    math.sin(self.goal_yaw - yaw),
                    math.cos(self.goal_yaw - yaw)
                )

                # 检查朝向误差是否在容差范围内
                if abs(yaw_error) > self.goal_yaw_tolerance:
                    cmd = Twist()
                    cmd.linear.x = 0.0

                    # 计算旋转角速度
                    w = self.final_rotate_kp * yaw_error
                    w = clamp(
                        w,
                        -self.final_rotate_max_yaw_rate,
                        self.final_rotate_max_yaw_rate
                    )

                    # 设置最小旋转速度
                    if abs(w) < self.final_rotate_min_yaw_rate:
                        w = math.copysign(self.final_rotate_min_yaw_rate, w)

                    cmd.angular.z = w
                    self.cmd_pub.publish(cmd)
                    return

            # 完全到达目标，停止运动
            self.publish_stop()
            self.log_periodic(
                'info',
                f'Goal reached at ({goal[0]:.2f}, {goal[1]:.2f}) from {self.goal_source}',
                'last_goal_reached_log_sec',
                2.0,
            )
            return

        # 将目标转换到机器人局部坐标系
        goal_local = self.goal_to_local(goal_dx, goal_dy, yaw)
        target_angle = math.atan2(goal_local[1], goal_local[0])

        # 计算朝向误差
        angle_error = math.atan2(math.sin(target_angle), math.cos(target_angle))
        abs_error = abs(angle_error)

        # 检查是否需要进入旋转模式
        if not self.rotating_to_goal and abs_error > self.rotate_to_goal_enter_angle:
            self.rotating_to_goal = True

        # 检查是否可以退出旋转模式
        if self.rotating_to_goal and abs_error < self.rotate_to_goal_exit_angle:
            self.rotating_to_goal = False

        # 执行旋转模式
        if self.rotating_to_goal:
            cmd = Twist()
            cmd.linear.x = 0.0

            # 检查角度死区
            if abs_error < self.rotate_angle_deadband:
                cmd.angular.z = 0.0
            else:
                # 计算旋转角速度
                raw_w = self.rotate_kp * angle_error
                raw_w = clamp(raw_w, -self.rotate_max_yaw_rate, self.rotate_max_yaw_rate)

                # 设置最小旋转速度
                if abs(raw_w) < self.rotate_min_yaw_rate:
                    raw_w = math.copysign(self.rotate_min_yaw_rate, raw_w)

                cmd.angular.z = raw_w

            self.cmd_pub.publish(cmd)
            self.publish_path([])
            return

        # 执行DWA算法选择最佳轨迹
        best = self.select_best_command(goal_local)
        if best is None:
            # 没有找到安全轨迹，执行避障旋转
            escape_cmd = self.build_escape_command()
            self.cmd_pub.publish(escape_cmd)
            self.publish_path([])
            self.log_periodic(
                'warn',
                'No safe DWA trajectory found, switching to escape rotation.',
                'last_escape_log_sec',
                1.0,
            )
            return

        # 发布最佳轨迹对应的控制指令
        best_v, best_w, best_traj = best
        cmd = Twist()
        cmd.linear.x = best_v
        cmd.angular.z = best_w
        self.cmd_pub.publish(cmd)
        self.publish_path(best_traj)

    def get_active_goal(self) -> Optional[Tuple[float, float]]:
        """
        获取当前激活的目标
        
        Returns:
            目标位置(x, y)或None
        """
        if self.goal_xy is not None:
            return self.goal_xy
        if self.use_static_goal:
            return (self.static_goal_x, self.static_goal_y)
        return None

    def goal_to_local(self, goal_dx: float, goal_dy: float, yaw: float) -> Tuple[float, float]:
        """
        将全局坐标系的目标转换到机器人局部坐标系
        
        Args:
            goal_dx: 目标在全局坐标系的x方向偏移
            goal_dy: 目标在全局坐标系的y方向偏移
            yaw: 机器人当前朝向
            
        Returns:
            目标在局部坐标系的位置(x, y)
        """
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)
        local_x = cos_yaw * goal_dx + sin_yaw * goal_dy
        local_y = -sin_yaw * goal_dx + cos_yaw * goal_dy
        return (local_x, local_y)

    def select_best_command(
        self,
        goal_local: Tuple[float, float],
    ) -> Optional[Tuple[float, float, Sequence[Tuple[float, float, float]]]]:
        """
        使用DWA算法选择最佳控制指令
        
        Args:
            goal_local: 局部坐标系下的目标位置
            
        Returns:
            最佳线速度、角速度和轨迹，或None(未找到安全轨迹)
        """
        current_v, current_w = self.current_velocity
        dt = max(self.last_control_dt, 1.0 / self.control_rate)

        # 计算动态窗口
        v_lower = clamp(current_v - self.max_accel * dt, self.min_speed, self.max_speed)
        v_upper = clamp(current_v + self.max_accel * dt, self.min_speed, self.max_speed)
        w_lower = clamp(current_w - self.max_yaw_accel * dt, -self.max_yaw_rate, self.max_yaw_rate)
        w_upper = clamp(current_w + self.max_yaw_accel * dt, -self.max_yaw_rate, self.max_yaw_rate)

        # 生成速度采样
        linear_candidates = self.linspace(v_lower, v_upper, self.v_samples)
        angular_candidates = self.linspace(w_lower, w_upper, self.w_samples)

        best_score = -1.0
        best_result: Optional[Tuple[float, float, Sequence[Tuple[float, float, float]]]] = None

        # 遍历所有速度组合
        for linear_vel in linear_candidates:
            for angular_vel in angular_candidates:
                # 模拟轨迹
                trajectory = self.simulate_trajectory(linear_vel, angular_vel)
                # 评估轨迹安全性
                valid, clearance = self.evaluate_clearance(trajectory)
                if not valid:
                    continue

                # 计算各项评分
                end_x, end_y, end_yaw = trajectory[-1]
                progress = self.compute_progress_score(goal_local, end_x, end_y)  # 进度评分
                clearance_score = clamp(clearance / self.clearance_cap, 0.0, 1.0)  # 安全距离评分
                velocity_score = clamp(linear_vel / max(self.max_speed, 1e-6), 0.0, 1.0)  # 速度评分
                heading_alignment = self.compute_heading_alignment(goal_local, end_x, end_y, end_yaw)  # 朝向评分

                # 综合评分
                score = (
                    self.heading_weight * (0.7 * progress + 0.3 * heading_alignment) +
                    self.clearance_weight * clearance_score +
                    self.velocity_weight * velocity_score
                )

                # 更新最佳结果
                if score > best_score:
                    best_score = score
                    best_result = (linear_vel, angular_vel, trajectory)

        return best_result

    def simulate_trajectory(self, linear_vel: float, angular_vel: float) -> List[Tuple[float, float, float]]:
        """
        模拟给定速度下的轨迹
        
        Args:
            linear_vel: 线速度
            angular_vel: 角速度
            
        Returns:
            模拟轨迹点列表[(x, y, yaw)]
        """
        x = 0.0
        y = 0.0
        yaw = 0.0
        trajectory = [(x, y, yaw)]  # 起始点
        steps = max(1, int(self.predict_time / self.sim_dt))  # 计算步数

        # 模拟轨迹
        for _ in range(steps):
            x += linear_vel * math.cos(yaw) * self.sim_dt
            y += linear_vel * math.sin(yaw) * self.sim_dt
            yaw += angular_vel * self.sim_dt
            trajectory.append((x, y, yaw))

        return trajectory

    def evaluate_clearance(self, trajectory: Sequence[Tuple[float, float, float]]) -> Tuple[bool, float]:
        """
        评估轨迹的安全性
        
        Args:
            trajectory: 待评估轨迹
            
        Returns:
            (是否安全, 最小安全距离)
        """
        if not self.obstacle_points:
            return True, self.clearance_cap

        collision_distance = self.robot_radius + self.safety_margin  # 碰撞距离
        min_clearance = self.clearance_cap  # 最小安全距离

        # 检查轨迹上的每个点
        for x, y, _ in trajectory:
            for obs_x, obs_y in self.obstacle_points:
                distance = math.hypot(obs_x - x, obs_y - y)
                if distance < collision_distance:
                    return False, 0.0  # 发生碰撞
                min_clearance = min(min_clearance, distance - collision_distance)

        return True, max(0.0, min_clearance)

    def compute_progress_score(self, goal_local: Tuple[float, float], end_x: float, end_y: float) -> float:
        """
        计算轨迹的进度评分
        
        Args:
            goal_local: 局部坐标系目标
            end_x: 轨迹终点x坐标
            end_y: 轨迹终点y坐标
            
        Returns:
            进度评分(0-1)
        """
        start_distance = math.hypot(goal_local[0], goal_local[1])  # 起始距离
        end_distance = math.hypot(goal_local[0] - end_x, goal_local[1] - end_y)  # 终点距离
        if start_distance < 1e-6:
            return 1.0
        return clamp((start_distance - end_distance) / start_distance, 0.0, 1.0)  # 距离减少比例

    def compute_heading_alignment(
        self,
        goal_local: Tuple[float, float],
        end_x: float,
        end_y: float,
        end_yaw: float,
    ) -> float:
        """
        计算轨迹终点的朝向对齐评分
        
        Args:
            goal_local: 局部坐标系目标
            end_x: 轨迹终点x坐标
            end_y: 轨迹终点y坐标
            end_yaw: 轨迹终点朝向
            
        Returns:
            朝向对齐评分(0-1)
        """
        target_heading = math.atan2(goal_local[1] - end_y, goal_local[0] - end_x)  # 目标方向
        error = math.atan2(math.sin(target_heading - end_yaw), math.cos(target_heading - end_yaw))  # 朝向误差
        return 1.0 - clamp(abs(error) / math.pi, 0.0, 1.0)  # 误差越小评分越高

    def build_escape_command(self) -> Twist:
        """
        构建避障旋转指令
        
        Returns:
            避障旋转指令
        """
        cmd = Twist()
        cmd.linear.x = 0.0  # 停止前进

        if self.latest_scan is None:
            cmd.angular.z = self.escape_yaw_rate  # 默认旋转方向
            return cmd

        # 分析前方障碍物分布
        left_clearance = 0.0
        right_clearance = 0.0
        left_count = 0
        right_count = 0
        angle = self.latest_scan.angle_min
        
        # 统计左右两侧的障碍物距离
        for distance in self.latest_scan.ranges:
            if math.isfinite(distance) and 0.0 < distance < self.front_sector_range:
                if 0.0 <= angle <= self.front_sector_half_angle:
                    left_clearance += distance
                    left_count += 1
                elif -self.front_sector_half_angle <= angle < 0.0:
                    right_clearance += distance
                    right_count += 1
            angle += self.latest_scan.angle_increment

        # 计算平均距离
        left_avg = left_clearance / left_count if left_count else 0.0
        right_avg = right_clearance / right_count if right_count else 0.0
        
        # 选择更空旷的方向旋转
        cmd.angular.z = self.escape_yaw_rate if left_avg >= right_avg else -self.escape_yaw_rate
        return cmd

    def publish_stop(self) -> None:
        """发布停止指令"""
        self.cmd_pub.publish(Twist())

    def log_periodic(self, level: str, message: str, attr_name: str, interval_sec: float) -> None:
        """
        周期性日志记录，避免日志过多
        
        Args:
            level: 日志级别
            message: 日志消息
            attr_name: 时间戳属性名
            interval_sec: 记录间隔(秒)
        """
        now_sec = self.get_clock().now().nanoseconds / 1e9
        last_sec = getattr(self, attr_name)

        # 检查是否达到记录间隔
        if last_sec >= 0.0 and now_sec - last_sec < interval_sec:
            return

        # 记录日志
        if level == 'debug':
            self.get_logger().debug(message)
        elif level == 'info':
            self.get_logger().info(message)
        elif level == 'warn':
            self.get_logger().warn(message)
        elif level == 'error':
            self.get_logger().error(message)
        else:
            self.get_logger().info(message)

        setattr(self, attr_name, now_sec)  # 更新时间戳

    def publish_path(self, local_trajectory: Sequence[Tuple[float, float, float]]) -> None:
        """
        发布规划路径
        
        Args:
            local_trajectory: 局部坐标系下的轨迹
        """
        path = Path()
        path.header.stamp = self.get_clock().now().to_msg()
        path.header.frame_id = self.goal_frame

        if self.current_pose is None:
            self.path_pub.publish(path)
            return

        # 将局部轨迹转换到全局坐标系
        base_x, base_y, base_yaw = self.current_pose
        cos_yaw = math.cos(base_yaw)
        sin_yaw = math.sin(base_yaw)

        for local_x, local_y, local_yaw in local_trajectory:
            pose = PoseStamped()
            pose.header = path.header
            # 坐标变换
            pose.pose.position.x = base_x + local_x * cos_yaw - local_y * sin_yaw
            pose.pose.position.y = base_y + local_x * sin_yaw + local_y * cos_yaw
            pose.pose.position.z = 0.0
            # 朝向变换
            yaw = base_yaw + local_yaw
            pose.pose.orientation.z = math.sin(yaw / 2.0)
            pose.pose.orientation.w = math.cos(yaw / 2.0)
            path.poses.append(pose)

        self.path_pub.publish(path)

    @staticmethod
    def linspace(lower: float, upper: float, count: int) -> List[float]:
        """
        生成等间距数值序列
        
        Args:
            lower: 下限
            upper: 上限
            count: 数量
            
        Returns:
            等间距数值列表
        """
        if count <= 1:
            return [upper]
        if abs(upper - lower) < 1e-6:
            return [lower for _ in range(count)]
        step = (upper - lower) / float(count - 1)
        return [lower + index * step for index in range(count)]


def main(args=None) -> None:
    """
    主函数
    初始化并运行DWA局部规划器
    """
    rclpy.init(args=args)
    node = DwaLocalPlanner()
    try:
        rclpy.spin(node)  # 运行节点
    except KeyboardInterrupt:
        pass
    finally:
        node.publish_stop()  # 停止运动
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()