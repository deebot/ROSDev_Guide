#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist


class TurtleTwistPub(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("turtle_twist") # MODIFY NAME
        self.publisher_= self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.timer_ =self.create_timer(0.5,self.publish_news)
        self.get_logger().info("velocity publisher started")
    def publish_news(self):
        msg = Twist()
        msg.linear.x = -2.0
        msg.linear.y = -2.0
        msg.linear.z =0.0
        msg.angular.x = 0.0
        msg.angular.y = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
       

def main(args=None):
    rclpy.init(args=args)
    node = TurtleTwistPub() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()