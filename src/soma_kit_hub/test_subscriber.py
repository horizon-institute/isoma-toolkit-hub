import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

import websocket

MOTOR_ACTUATOR_IP = "10.223.130.212"


class MotorActuatorSubscriber(Node):

    def __init__(self):
        super().__init__('motor_actuator_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/oas/soma_kit/motor_actuator/id_1',
            self.listener_callback,
            10)
        self.ws = websocket.WebSocket()
        self.ws.connect(f"ws://{MOTOR_ACTUATOR_IP}/ws")

    def listener_callback(self, msg):
        self.ws.send(str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    ma_subscriber = MotorActuatorSubscriber()
    rclpy.spin(ma_subscriber)
    ma_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
