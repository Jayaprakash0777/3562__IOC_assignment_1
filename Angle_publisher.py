#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import time

class AnglePublisher(Node):
    def __init__(self):
        super().__init__('angle_publisher')
        self.publisher_ = self.create_publisher(Float32, 'joint_angle', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.angle = 0.0
        self.get_logger().info("Angle Publisher Node Started")

    def timer_callback(self):
        # simulate a moving angle (0°–180°)
        self.angle = (self.angle + 30.0) % 180.0
        msg = Float32()
        msg.data = self.angle
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing angle: {self.angle:.2f}°')

def main(args=None):
    rclpy.init(args=args)
    node = AnglePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
