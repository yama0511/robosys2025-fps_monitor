# fps_monitor

[![test](https://github.com/yama0511/robosys2025-fps_monitor/actions/workflows/test.yml/badge.svg)](https://github.com/yama0511/robosys2025-fps_monitor/actions/workflows/test.yml)

センサーデータの受信間隔からフレームレート（FPS）を計算・監視するROS 2パッケージです。
変動するセンサーデータの受信頻度をリアルタイムで計測し、現在値と平均値をログ表示およびトピック配信します。


## 環境
* Ubuntu 22.04 LTS
* ROS 2 Humble
* Python 3.10

## インストール
```bash
cd ~/ros2_ws/src
git clone [https://github.com/yama0511/robosys2025-fps_monitor.git](https://github.com/yama0511/robosys2025-fps_monitor.git)
cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro humble -y
colcon build --packages-select fps_monitor
source install/setup.bash
```

## 実行方法
### 1. シミュレーションと計算の同時実行（推奨）
Launchファイルを使用して、センサーシミュレータと計算ノードを同時に起動します。
```Bash
ros2 launch fps_monitor fps_launch.py
```

### 2. 個別に実行する場合
端末1: センサーシミュレータ（データ送信）
```Bash
ros2 run fps_monitor sensor_sim
```
端末2: FPS計算（データ受信・表示）
```Bash
ros2 run fps_monitor fps_calc
```

## 確認方法（rqt_plot）
グラフでFPSの変動を確認できます。

### 1. ros2 launch fps_monitor fps_launch.py を実行中に、新しい端末を開く。

### 2. 以下のコマンドを実行。
```Bash
ros2 run rqt_plot rqt_plot
```
### 3. Topic欄に /current_fps/data と入力して追加する。

## ライセンス
このソフトウェアは、BSD 3-Clause License の下で公開されています。 詳細については LICENSE をご確認ください。

© 2025 Yamato Okada
