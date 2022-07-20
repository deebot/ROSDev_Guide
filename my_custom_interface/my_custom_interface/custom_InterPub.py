#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from rex_interfaces.msg import RobotData

class telemetryPublisherNode(Node):
    def __init__(self):
        super().__init__("custom_InterPub")
        self.hw_status_publisher_ = self.create_publisher(RobotData, "RobotTelemetry", 10)
        self.timer_ = self.create_timer(1.0, self.publish_sensor_status)
        self.get_logger().info("Telemetry publisher has been started.")

    def publish_sensor_status(self):
        msg = RobotData()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = "No Errors detected"
        self.hw_status_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = telemetryPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

