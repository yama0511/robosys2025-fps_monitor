# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorSim(Node):

    def __init__(self):
        super().__init__('sensor_sim')
        self.publisher_ = self.create_publisher(Float32, 'sensor_data', 10)
        self.timer_period = 0.033
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 100.0)
        self.publisher_.publish(msg)

        self.timer.cancel()
        self.timer_period = random.uniform(0.016, 0.1)
        self.timer = self.create_timer(self.timer_period, self.timer_callback)


def main(args=None):
    rclpy.init(args=args)
    node = SensorSim()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
