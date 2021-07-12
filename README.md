# raspi_realtime-matplot

ラズベリーパイでセンサーから温度を取得して
リアルタイムでグラフに表示する。

## 使用方法
### 依存ライブラリをインストール

```
pip3 install --upgrade Pillow==6.2.1
pip3 install matplotlib
```
### raspberryOSの場合には
```
pip3 install matplotlib
sudo apt-get install libatlas-base-dev
sudo apt-get install python3-gi-cairo
```
## matplotlibでリアルタイムのデータを表示する

```
git clone https://github.com/kmchord9/raspi_realtime-matplot.git
cd raspi_realtime-matplot
python3 temp.py
```
初期状態はrandomTempの関数でダーミーデータを表示している。
adt7410_13bit.pyにadt7410の温度センサーから温度を取得する関数があるので、
randomTempをdt7410の温度センサーから温度を取得する関数に置き換えると
温度を表示できる。

※事前にadt7410センサーからi2c通信でセンサーを認識していることを前提とする
