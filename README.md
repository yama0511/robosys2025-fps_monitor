# robosys2025_fps_monitor

[![test](https://github.com/yama0511/robosys2025_fps_monitor/actions/workflows/test.yml/badge.svg)](https://github.com/yama0511/robosys2025_fps_monitor/actions/workflows/test.yml)

センサーデータの受信間隔からフレームレート（FPS）を計算・監視するROS 2パッケージです。
変動するセンサーデータの受信頻度をリアルタイムで計測し、現在値と平均値をログ表示およびトピック配信します。


## 環境
* Ubuntu 22.04 LTS
* ROS 2 Humble
* Python 3.10

## ノードとトピック
### sensor_sim
センサーデータを模した値をランダムな間隔 (約10Hz〜60Hz) で送信するシミュレータノードです。

* **Publishers**
  * `/sensor_data` (std_msgs/msg/Float32): 疑似センサーデータ

### fps_calc
受信したセンサーデータの時間間隔からフレームレート (FPS) をリアルタイムで計算するノードです。

* **Subscribers**
  * `/sensor_data` (std_msgs/msg/Float32): 疑似センサーデータ
* **Publishers**
  * `/current_fps` (std_msgs/msg/Float32): 計算された現在のFPS値

## インストール
ROS 2 ワークスペースの `src` ディレクトリに本リポジトリをクローンし、ワークスペースのルートディレクトリでビルドしてください。
```bash
# リポジトリのクローン
git clone [https://github.com/yama0511/robosys2025_fps_monitor.git](https://github.com/yama0511/robosys2025_fps_monitor.git)

# 依存関係のインストールとビルド
rosdep install -i --from-path src --rosdistro humble -y
colcon build --packages-select robosys2025_fps_monitor

# セットアップファイルの読み込み
source install/setup.bash
```

#### 3. 保存してプッシュ
```bash
cd ~/ros2_ws/src/robosys2025_fps_monitor
git add README.md
git commit -m "Update install instructions to generic style"
git push
```

## 実行方法
### 1. Launchファイルによる実行
Launchファイルを使用して、センサーシミュレータと計算ノードを同時に起動します。
```Bash
ros2 launch robosys2025_fps_monitor fps_launch.py
```

### 2. 個別に実行する場合
端末1: センサーシミュレータ（データ送信）
```Bash
ros2 run robosys2025_fps_monitor sensor_sim
```
端末2: FPS計算（データ受信・表示）
```Bash
ros2 run robosys2025_fps_monitor fps_calc
```

## 確認方法（rqt_plot）
グラフでFPSの変動を確認できます。

1. ros2 launch robosys2025_fps_monitor fps_launch.py を実行中に、新しい端末を開く。

2. 以下のコマンドを実行。
```Bash
ros2 run rqt_plot rqt_plot
```
3. 起動した rqt_plot ウィンドウの画面上部にある Topic 入力欄に /current_fps/data と入力し、右側の + ボタンを押してグラフを表示させる。

## ライセンス
このソフトウェアは、BSD 3-Clause License の下で公開されています。 詳細については LICENSE をご確認ください。

© 2025 Yamato Okada
