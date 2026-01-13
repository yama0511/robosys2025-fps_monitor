#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Yamato Okada
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo ${1}行目が違うよ
      res=1
}

res=0

source /opt/ros/humble/setup.bash

colcon build --packages-select robosys2025_fps_monitor || ng "$LINENO"
source install/setup.bash

timeout 10 ros2 launch robosys2025_fps_monitor fps_launch.py > /tmp/robosys2025_fps_monitor.log 2>&1 || true

count=$(grep -c "FPS" /tmp/robosys2025_fps_monitor.log)
[ "$count" -ge 1 ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK

exit $res
