#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from visualization_msgs.msg import Marker


class GearMarkerPublisher(Node):
    def __init__(self):
        super().__init__('gear_marker_publisher')

        self.current_level = "0"

        self.subscription = self.create_subscription(
            String,
            '/mower/cutting_motor/status',
            self.status_callback,
            10
        )

        self.marker_publisher = self.create_publisher(
            Marker,
            '/mower/gear_marker',
            10
        )

        self.timer = self.create_timer(0.1, self.publish_marker)

        self.get_logger().info('Gear marker publisher started')

    def status_callback(self, msg: String):
        self.current_level = msg.data

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = 'base_link'
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = 'gear_display'
        marker.id = 0
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD

        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.45
        marker.pose.orientation.w = 1.0

        marker.scale.z = 0.12

        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0

        marker.text = f'GEAR {self.current_level}'

        self.marker_publisher.publish(marker)


def main(args=None):
    rclpy.init(args=args)
    node = GearMarkerPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
