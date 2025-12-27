# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from collections import deque
import time


class FpsCalc(Node):

    def __init__(self):
        super().__init__('fps_calc')

        self.subscription = self.create_subscription(
            Float32,
            'sensor_data',
            self.listener_callback,
            10)
        
        self.pub_fps = self.create_publisher(Float32, 'current_fps', 10)

        self.last_time = time.time()
        self.fps_history = deque(maxlen=50)

    def listener_callback(self, msg):
        current_time = time.time()
        delta = current_time - self.last_time
        self.last_time = current_time

        if delta > 0:
            current_fps = 1.0 / delta
            self.fps_history.append(current_fps)

            avg_fps = sum(self.fps_history) / len(self.fps_history)

            self.get_logger().info(
                f'Current: {current_fps:.1f} Hz | Avg: {avg_fps:.1f} Hz'
            )

            fps_msg = Float32()
            fps_msg.data = current_fps
            self.pub_fps.publish(fps_msg)


def main(args=None):
    rclpy.init(args=args)
    node = FpsCalc()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
