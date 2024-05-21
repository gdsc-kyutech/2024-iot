# 2024-iot

## Table of Contents

### Basic 🔰

##### [1. Pico Wのセットアップ](1-setup.md)

1. Thonnyをインストール
1. Pico Wを接続
1. ファームウェアを焼き込み
1. Lチカ (local)
1. Lチカ (Wi-Fi)

##### [2. LINE Notify を利用した簡易Botの開発](2-simple-bot.md)

1. LINE Notify アクセストークンの取得
1. 本体温度センサを利用した通知デモ
1. (Optional) GPIOを利用した温度監視システムの構築

###  Intermediate

##### [3-a. LINE Messaging API を利用した本格Botの開発 (前半)](3-a-practical-bot.md)

1. LINE Developersアカウントの作成
1. Messaging API利用のための初期設定
1. Google Apps Scriptを書いてみる
1. Webhook URLの設定
1. メッセージ内容に応じた処理の分岐

##### [3-b. LINE Messaging API を利用した本格Botの開発 (後半)](3-b-practical-bot.md)

1. Pico Wとの連携
1. Botのカスタマイズ

### Advanced

##### [(a) MQTT・クラウドサービスを使った本格IoT](4-mqtt.md)

1. Mosquitoを使ってMQTTを試す
1. Microsoft Azure IoT Hubで時系列データを見る

##### [(b) 他のボードやセンサ，ディスプレイなどを試してみる](4-other.md)

M5StackやArdiono，その他各種電子部品をご用意しています．  
詳しくは上記リンクからご確認ください．

## Sources

- **[スライド](slide.pdf)**  
講座で使用したスライドです．

- **[イベント録画](https://youtu.be/Ic1-McBGZow)**  
本資料を用いて，2024/05/11(土)に九州工業大学飯塚キャンパスポルト棟にてハンズオンイベントを開催しました．  
イベント詳細は[こちら](https://gdsc.community.dev/events/details/developer-student-clubs-kyushu-institute-of-technology-fukuoka-japan-presents-razupaipico-wgamoraerulinewoshi-tsutaiothanzuon/)から

## FAQ

### ThonnyでBackend Errorが表示されてPico Wを認識しない

メモリ領域に不要なファイルが残っている場合があります．  

1. [こちらの初期化用イメージ](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)をダウンロードし，ファームウェアと同様に書き込み
1. 再度，通常のファームウェアを書き込み  

で復旧できます．

// `terubouzu`さん，ありがとうございました！

### ThonnyとPico Wの接続がうまくいかない

以下の手順をお試しください．  
途中で接続に成功すれば，以降のステップを踏む必要はありません．

1. 赤い停止ボタンを3回ほど押してみる
1. 一旦USBケーブルを抜き，再度接続してみる
1. Thonnyを開き，右下の`MicroPython`を一旦`ローカルPython`に変更，再度`MicroPython`に変更してみる
1. Thonnyを一旦閉じて，再度起動してみる
1. 一旦USBケーブルを抜き，ボタンを押しながら接続して再度ファームウェアを焼いてみる
1. PCを再起動してみる

### LINEに送る文字列が文字化けする

Windows環境において発生するようです．  
システムの文字コードを`Shift-JIS`から`UTF-8`に変更することで改善します．  
[こちら](https://otona-life.com/2022/06/05/121603/)を参考にお試しください．

なお，その他のプログラムにも影響を及ぼします．  
もし正常に動かなくなってしまった場合は，再度`Shift-JIS`へお戻しください．
