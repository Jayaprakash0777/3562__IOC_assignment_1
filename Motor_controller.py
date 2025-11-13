#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(
            Float32,
            'joint_angle',
            self.listener_callback,
            10)
        self.subscription
        self.get_logger().info("Motor Controller Node Started")

    def listener_callback(self, msg):
        self.get_logger().info(f'Received target angle: {msg.data:.2f}° — Moving motor...')

def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
