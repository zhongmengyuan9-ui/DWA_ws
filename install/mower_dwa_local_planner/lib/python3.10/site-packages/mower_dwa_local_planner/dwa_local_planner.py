import math
from typing import List, Optional, Sequence, Tuple

import rclpy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Twist
from nav_msgs.msg import Odometry, Path
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def yaw_from_quaternion(x: float, y: float, z: float, w: float) -> float:
    siny_cosp = 2.0 * (w * z + x * y)
    cosy_cosp = 1.0 - 2.0 * (y * y + z * z)
    return math.atan2(siny_cosp, cosy_cosp)


class DwaLocalPlanner(Node):
    def __init__(self) -> None:
        super().__init__('dwa_local_planner')

        self.declare_parameter('goal_yaw_tolerance', 0.15)
        self.declare_parameter('final_rotate_kp', 0.8)
        self.declare_parameter('final_rotate_max_yaw_rate', 0.5)
        self.declare_parameter('final_rotate_min_yaw_rate', 0.08)
        self.declare_parameter('rotate_to_goal_enter_angle', 1.75)
        self.declare_parameter('rotate_to_goal_exit_angle', 0.35)
        self.declare_parameter('rotate_kp', 0.8)
        self.declare_parameter('rotate_max_yaw_rate', 0.6)
        self.declare_parameter('rotate_min_yaw_rate', 0.12)
        self.declare_parameter('rotate_angle_deadband', 0.08)
        self.declare_parameter('scan_topic', '/scan')
        self.declare_parameter('odom_topic', '/odom')
        self.declare_parameter('cmd_vel_topic', '/cmd_vel')
        self.declare_parameter('goal_topic', '/goal_pose')
        self.declare_parameter('path_topic', '/dwa/best_path')
        self.declare_parameter('goal_frame', 'odom')
        self.declare_parameter('use_static_goal', False)
        self.declare_parameter('static_goal_x', 3.0)
        self.declare_parameter('static_goal_y', 0.0)
        self.declare_parameter('goal_tolerance', 0.35)
        self.declare_parameter('control_rate', 10.0)
        self.declare_parameter('predict_time', 2.5)
        self.declare_parameter('sim_dt', 0.1)
        self.declare_parameter('v_samples', 8)
        self.declare_parameter('w_samples', 17)
        self.declare_parameter('min_speed', 0.0)
        self.declare_parameter('max_speed', 0.7)
        self.declare_parameter('max_yaw_rate', 1.4)
        self.declare_parameter('max_accel', 0.7)
        self.declare_parameter('max_yaw_accel', 2.2)
        self.declare_parameter('robot_radius', 0.38)
        self.declare_parameter('safety_margin', 0.12)
        self.declare_parameter('clearance_cap', 2.5)
        self.declare_parameter('obstacle_range', 6.0)
        self.declare_parameter('heading_weight', 0.52)
        self.declare_parameter('clearance_weight', 0.30)
        self.declare_parameter('velocity_weight', 0.18)
        self.declare_parameter('escape_yaw_rate', 0.6)
        self.declare_parameter('front_sector_half_angle', 0.55)
        self.declare_parameter('front_sector_range', 1.5)

        self.goal_yaw_tolerance = float(self.get_parameter('goal_yaw_tolerance').value)
        self.final_rotate_kp = float(self.get_parameter('final_rotate_kp').value)
        self.final_rotate_max_yaw_rate = float(self.get_parameter('final_rotate_max_yaw_rate').value)
        self.final_rotate_min_yaw_rate = float(self.get_parameter('final_rotate_min_yaw_rate').value)
        self.rotate_to_goal_enter_angle = float(self.get_parameter('rotate_to_goal_enter_angle').value)
        self.rotate_to_goal_exit_angle = float(self.get_parameter('rotate_to_goal_exit_angle').value)
        self.rotate_kp = float(self.get_parameter('rotate_kp').value)
        self.rotate_max_yaw_rate = float(self.get_parameter('rotate_max_yaw_rate').value)
        self.rotate_min_yaw_rate = float(self.get_parameter('rotate_min_yaw_rate').value)
        self.rotate_angle_deadband = float(self.get_parameter('rotate_angle_deadband').value)
        self.scan_topic = self.get_parameter('scan_topic').value
        self.odom_topic = self.get_parameter('odom_topic').value
        self.cmd_vel_topic = self.get_parameter('cmd_vel_topic').value
        self.goal_topic = self.get_parameter('goal_topic').value
        self.path_topic = self.get_parameter('path_topic').value
        self.goal_frame = self.get_parameter('goal_frame').value
        self.use_static_goal = bool(self.get_parameter('use_static_goal').value)
        self.static_goal_x = float(self.get_parameter('static_goal_x').value)
        self.static_goal_y = float(self.get_parameter('static_goal_y').value)
        self.goal_tolerance = float(self.get_parameter('goal_tolerance').value)
        self.control_rate = float(self.get_parameter('control_rate').value)
        self.predict_time = float(self.get_parameter('predict_time').value)
        self.sim_dt = float(self.get_parameter('sim_dt').value)
        self.v_samples = max(2, int(self.get_parameter('v_samples').value))
        self.w_samples = max(3, int(self.get_parameter('w_samples').value))
        self.min_speed = float(self.get_parameter('min_speed').value)
        self.max_speed = float(self.get_parameter('max_speed').value)
        self.max_yaw_rate = float(self.get_parameter('max_yaw_rate').value)
        self.max_accel = float(self.get_parameter('max_accel').value)
        self.max_yaw_accel = float(self.get_parameter('max_yaw_accel').value)
        self.robot_radius = float(self.get_parameter('robot_radius').value)
        self.safety_margin = float(self.get_parameter('safety_margin').value)
        self.clearance_cap = float(self.get_parameter('clearance_cap').value)
        self.obstacle_range = float(self.get_parameter('obstacle_range').value)
        self.heading_weight = float(self.get_parameter('heading_weight').value)
        self.clearance_weight = float(self.get_parameter('clearance_weight').value)
        self.velocity_weight = float(self.get_parameter('velocity_weight').value)
        self.escape_yaw_rate = float(self.get_parameter('escape_yaw_rate').value)
        self.front_sector_half_angle = float(self.get_parameter('front_sector_half_angle').value)
        self.front_sector_range = float(self.get_parameter('front_sector_range').value)

        self.current_pose: Optional[Tuple[float, float, float]] = None
        self.current_velocity: Tuple[float, float] = (0.0, 0.0)
        self.goal_xy: Optional[Tuple[float, float]] = None
        self.goal_yaw: Optional[float] = None
        self.goal_source = 'static' if self.use_static_goal else 'unset'
        self.obstacle_points: List[Tuple[float, float]] = []
        self.latest_scan: Optional[LaserScan] = None
        self.last_control_dt = 1.0 / self.control_rate
        self.last_loop_time = self.get_clock().now()
        self.reported_waiting = False
        self.last_no_goal_log_sec = -1.0
        self.last_escape_log_sec = -1.0
        self.last_goal_reached_log_sec = -1.0
        self.last_invalid_goal_log_sec = -1.0
        self.rotating_to_goal = False

        self.cmd_pub = self.create_publisher(Twist, self.cmd_vel_topic, 10)
        self.path_pub = self.create_publisher(Path, self.path_topic, 10)
        self.goal_echo_pub = self.create_publisher(PoseWithCovarianceStamped, '/dwa/goal_echo', 10)

        self.create_subscription(LaserScan, self.scan_topic, self.scan_callback, 10)
        self.create_subscription(Odometry, self.odom_topic, self.odom_callback, 10)
        self.create_subscription(PoseStamped, self.goal_topic, self.goal_callback, 10)
        self.timer = self.create_timer(1.0 / self.control_rate, self.control_loop)

        self.get_logger().info(
            f'DWA local planner started: scan={self.scan_topic}, odom={self.odom_topic}, '
            f'cmd_vel={self.cmd_vel_topic}, goal={self.goal_topic}'
        )

    def goal_callback(self, msg: PoseStamped) -> None:
        frame_id = msg.header.frame_id or self.goal_frame
        if frame_id != self.goal_frame:
            self.log_periodic(
                'warn',
                f'Ignore goal in frame "{frame_id}". Expected "{self.goal_frame}".',
                'last_invalid_goal_log_sec',
                2.0,
            )
            return

        self.goal_xy = (msg.pose.position.x, msg.pose.position.y)
        self.goal_yaw = yaw_from_quaternion(
            msg.pose.orientation.x,
            msg.pose.orientation.y,
            msg.pose.orientation.z,
            msg.pose.orientation.w
        )
        self.goal_source = 'topic'

        echo = PoseWithCovarianceStamped()
        echo.header = msg.header
        echo.pose.pose = msg.pose
        self.goal_echo_pub.publish(echo)

        self.get_logger().info(
            f'Received goal ({self.goal_xy[0]:.2f}, {self.goal_xy[1]:.2f}) in {frame_id}'
        )

    def odom_callback(self, msg: Odometry) -> None:
        pose = msg.pose.pose
        twist = msg.twist.twist
        yaw = yaw_from_quaternion(
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w,
        )
        self.current_pose = (pose.position.x, pose.position.y, yaw)
        self.current_velocity = (twist.linear.x, twist.angular.z)

    def scan_callback(self, msg: LaserScan) -> None:
        self.latest_scan = msg
        points: List[Tuple[float, float]] = []
        angle = msg.angle_min
        for distance in msg.ranges:
            if math.isfinite(distance) and msg.range_min < distance < min(msg.range_max, self.obstacle_range):
                points.append((distance * math.cos(angle), distance * math.sin(angle)))
            angle += msg.angle_increment
        self.obstacle_points = points

    def control_loop(self) -> None:
        now = self.get_clock().now()
        dt = (now - self.last_loop_time).nanoseconds / 1e9
        self.last_loop_time = now
        if dt > 1e-4:
            self.last_control_dt = dt

        if self.current_pose is None or self.latest_scan is None:
            if not self.reported_waiting:
                self.get_logger().info('Waiting for odom and scan data...')
                self.reported_waiting = True
            return

        self.reported_waiting = False
        goal = self.get_active_goal()
        if goal is None:
            self.publish_stop()
            self.publish_path([])
            self.log_periodic(
                'info',
                'No active goal. Send RViz 2D Goal Pose to /goal_pose or enable use_static_goal.',
                'last_no_goal_log_sec',
                5.0,
            )
            return

        x, y, yaw = self.current_pose
        goal_dx = goal[0] - x
        goal_dy = goal[1] - y
        goal_distance = math.hypot(goal_dx, goal_dy)
        if goal_distance <= self.goal_tolerance:
            self.publish_path([])

            if self.goal_yaw is not None:
                yaw_error = math.atan2(
                    math.sin(self.goal_yaw - yaw),
                    math.cos(self.goal_yaw - yaw)
                )

                if abs(yaw_error) > self.goal_yaw_tolerance:
                    cmd = Twist()
                    cmd.linear.x = 0.0

                    w = self.final_rotate_kp * yaw_error
                    w = clamp(
                        w,
                        -self.final_rotate_max_yaw_rate,
                        self.final_rotate_max_yaw_rate
                    )

                    if abs(w) < self.final_rotate_min_yaw_rate:
                        w = math.copysign(self.final_rotate_min_yaw_rate, w)

                    cmd.angular.z = w
                    self.cmd_pub.publish(cmd)
                    return

            self.publish_stop()
            self.log_periodic(
                'info',
                f'Goal reached at ({goal[0]:.2f}, {goal[1]:.2f}) from {self.goal_source}',
                'last_goal_reached_log_sec',
                2.0,
            )
            return


        goal_local = self.goal_to_local(goal_dx, goal_dy, yaw)
        target_angle = math.atan2(goal_local[1], goal_local[0])

        angle_error = math.atan2(math.sin(target_angle), math.cos(target_angle))
        abs_error = abs(angle_error)

        if not self.rotating_to_goal and abs_error > self.rotate_to_goal_enter_angle:
            self.rotating_to_goal = True

        if self.rotating_to_goal and abs_error < self.rotate_to_goal_exit_angle:
            self.rotating_to_goal = False

        if self.rotating_to_goal:
            cmd = Twist()
            cmd.linear.x = 0.0

            if abs_error < self.rotate_angle_deadband:
                cmd.angular.z = 0.0
            else:
                raw_w = self.rotate_kp * angle_error
                raw_w = clamp(raw_w, -self.rotate_max_yaw_rate, self.rotate_max_yaw_rate)

                if abs(raw_w) < self.rotate_min_yaw_rate:
                    raw_w = math.copysign(self.rotate_min_yaw_rate, raw_w)

                cmd.angular.z = raw_w

            self.cmd_pub.publish(cmd)
            self.publish_path([])
            return


        best = self.select_best_command(goal_local)
        if best is None:
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

        best_v, best_w, best_traj = best
        cmd = Twist()
        cmd.linear.x = best_v
        cmd.angular.z = best_w
        self.cmd_pub.publish(cmd)
        self.publish_path(best_traj)

    def get_active_goal(self) -> Optional[Tuple[float, float]]:
        if self.goal_xy is not None:
            return self.goal_xy
        if self.use_static_goal:
            return (self.static_goal_x, self.static_goal_y)
        return None

    def goal_to_local(self, goal_dx: float, goal_dy: float, yaw: float) -> Tuple[float, float]:
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)
        local_x = cos_yaw * goal_dx + sin_yaw * goal_dy
        local_y = -sin_yaw * goal_dx + cos_yaw * goal_dy
        return (local_x, local_y)

    def select_best_command(
        self,
        goal_local: Tuple[float, float],
    ) -> Optional[Tuple[float, float, Sequence[Tuple[float, float, float]]]]:
        current_v, current_w = self.current_velocity
        dt = max(self.last_control_dt, 1.0 / self.control_rate)

        v_lower = clamp(current_v - self.max_accel * dt, self.min_speed, self.max_speed)
        v_upper = clamp(current_v + self.max_accel * dt, self.min_speed, self.max_speed)
        w_lower = clamp(current_w - self.max_yaw_accel * dt, -self.max_yaw_rate, self.max_yaw_rate)
        w_upper = clamp(current_w + self.max_yaw_accel * dt, -self.max_yaw_rate, self.max_yaw_rate)

        linear_candidates = self.linspace(v_lower, v_upper, self.v_samples)
        angular_candidates = self.linspace(w_lower, w_upper, self.w_samples)

        best_score = -1.0
        best_result: Optional[Tuple[float, float, Sequence[Tuple[float, float, float]]]] = None

        for linear_vel in linear_candidates:
            for angular_vel in angular_candidates:
                trajectory = self.simulate_trajectory(linear_vel, angular_vel)
                valid, clearance = self.evaluate_clearance(trajectory)
                if not valid:
                    continue

                end_x, end_y, end_yaw = trajectory[-1]
                progress = self.compute_progress_score(goal_local, end_x, end_y)
                clearance_score = clamp(clearance / self.clearance_cap, 0.0, 1.0)
                velocity_score = clamp(linear_vel / max(self.max_speed, 1e-6), 0.0, 1.0)
                heading_alignment = self.compute_heading_alignment(goal_local, end_x, end_y, end_yaw)

                score = (
                    self.heading_weight * (0.7 * progress + 0.3 * heading_alignment) +
                    self.clearance_weight * clearance_score +
                    self.velocity_weight * velocity_score
                )

                if score > best_score:
                    best_score = score
                    best_result = (linear_vel, angular_vel, trajectory)

        return best_result

    def simulate_trajectory(self, linear_vel: float, angular_vel: float) -> List[Tuple[float, float, float]]:
        x = 0.0
        y = 0.0
        yaw = 0.0
        trajectory = [(x, y, yaw)]
        steps = max(1, int(self.predict_time / self.sim_dt))

        for _ in range(steps):
            x += linear_vel * math.cos(yaw) * self.sim_dt
            y += linear_vel * math.sin(yaw) * self.sim_dt
            yaw += angular_vel * self.sim_dt
            trajectory.append((x, y, yaw))

        return trajectory

    def evaluate_clearance(self, trajectory: Sequence[Tuple[float, float, float]]) -> Tuple[bool, float]:
        if not self.obstacle_points:
            return True, self.clearance_cap

        collision_distance = self.robot_radius + self.safety_margin
        min_clearance = self.clearance_cap

        for x, y, _ in trajectory:
            for obs_x, obs_y in self.obstacle_points:
                distance = math.hypot(obs_x - x, obs_y - y)
                if distance < collision_distance:
                    return False, 0.0
                min_clearance = min(min_clearance, distance - collision_distance)

        return True, max(0.0, min_clearance)

    def compute_progress_score(self, goal_local: Tuple[float, float], end_x: float, end_y: float) -> float:
        start_distance = math.hypot(goal_local[0], goal_local[1])
        end_distance = math.hypot(goal_local[0] - end_x, goal_local[1] - end_y)
        if start_distance < 1e-6:
            return 1.0
        return clamp((start_distance - end_distance) / start_distance, 0.0, 1.0)

    def compute_heading_alignment(
        self,
        goal_local: Tuple[float, float],
        end_x: float,
        end_y: float,
        end_yaw: float,
    ) -> float:
        target_heading = math.atan2(goal_local[1] - end_y, goal_local[0] - end_x)
        error = math.atan2(math.sin(target_heading - end_yaw), math.cos(target_heading - end_yaw))
        return 1.0 - clamp(abs(error) / math.pi, 0.0, 1.0)

    def build_escape_command(self) -> Twist:
        cmd = Twist()
        cmd.linear.x = 0.0

        if self.latest_scan is None:
            cmd.angular.z = self.escape_yaw_rate
            return cmd

        left_clearance = 0.0
        right_clearance = 0.0
        left_count = 0
        right_count = 0
        angle = self.latest_scan.angle_min
        for distance in self.latest_scan.ranges:
            if math.isfinite(distance) and 0.0 < distance < self.front_sector_range:
                if 0.0 <= angle <= self.front_sector_half_angle:
                    left_clearance += distance
                    left_count += 1
                elif -self.front_sector_half_angle <= angle < 0.0:
                    right_clearance += distance
                    right_count += 1
            angle += self.latest_scan.angle_increment

        left_avg = left_clearance / left_count if left_count else 0.0
        right_avg = right_clearance / right_count if right_count else 0.0
        cmd.angular.z = self.escape_yaw_rate if left_avg >= right_avg else -self.escape_yaw_rate
        return cmd

    def publish_stop(self) -> None:
        self.cmd_pub.publish(Twist())

    def log_periodic(self, level: str, message: str, attr_name: str, interval_sec: float) -> None:
        now_sec = self.get_clock().now().nanoseconds / 1e9
        last_sec = getattr(self, attr_name)

        if last_sec >= 0.0 and now_sec - last_sec < interval_sec:
            return

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

        setattr(self, attr_name, now_sec)


    def publish_path(self, local_trajectory: Sequence[Tuple[float, float, float]]) -> None:
        path = Path()
        path.header.stamp = self.get_clock().now().to_msg()
        path.header.frame_id = self.goal_frame

        if self.current_pose is None:
            self.path_pub.publish(path)
            return

        base_x, base_y, base_yaw = self.current_pose
        cos_yaw = math.cos(base_yaw)
        sin_yaw = math.sin(base_yaw)

        for local_x, local_y, local_yaw in local_trajectory:
            pose = PoseStamped()
            pose.header = path.header
            pose.pose.position.x = base_x + local_x * cos_yaw - local_y * sin_yaw
            pose.pose.position.y = base_y + local_x * sin_yaw + local_y * cos_yaw
            pose.pose.position.z = 0.0
            yaw = base_yaw + local_yaw
            pose.pose.orientation.z = math.sin(yaw / 2.0)
            pose.pose.orientation.w = math.cos(yaw / 2.0)
            path.poses.append(pose)

        self.path_pub.publish(path)

    @staticmethod
    def linspace(lower: float, upper: float, count: int) -> List[float]:
        if count <= 1:
            return [upper]
        if abs(upper - lower) < 1e-6:
            return [lower for _ in range(count)]
        step = (upper - lower) / float(count - 1)
        return [lower + index * step for index in range(count)]


def main(args=None) -> None:
    rclpy.init(args=args)
    node = DwaLocalPlanner()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publish_stop()
        node.destroy_node()
        rclpy.shutdown()
