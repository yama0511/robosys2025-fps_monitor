#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

ros2 launch robosys2025_fps_monitor fps_launch.py > /dev/null &
PID=$!
sleep 5

res=$(timeout 10 ros2 topic echo /current_fps --once)
kill $PID

echo "$res" | grep "data" && exit 0
exit 1
