import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

import websocket

PRESSURE_SENSOR_IP = "10.82.144.150"

class PressureSensorPublisher(Node):

    def __init__(self):
        super().__init__('pressure_sensor_publisher')
        self.publisher_ = self.create_publisher(Int32, '/oas/soma_kit/pressure_sensor/id_1', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.ws = websocket.WebSocket()
        self.ws.connect(f"ws://{PRESSURE_SENSOR_IP}/ws")

    def timer_callback(self):
        self.ws.send("gimme")
        msg = Int32()
        msg.data = int(self.ws.recv())
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    ps_publisher = PressureSensorPublisher()
    rclpy.spin(ps_publisher)
    ps_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
