# (a) MQTT・クラウドサービスを使った本格IoT

あなたはとある携帯電話会社のエンジニアです．
日本各地に設置した基地局設備の温度を，リアルタイムに計測するプロジェクトを1人で担うことになりました．
以下の要件に沿うようにシステムを構築してください．

- それぞれの基地局に1台のRaspberry Pi Pico Wを設置し，気温の計測・送信端末とすること
- 測定したデータはMQTTというプロトコルを用いてMicrosoft AzureのIoT Hubに送信し，集積すること
- 単一のPico Wから送信された気温を，時系列データとしてグラフで表示できること

参考になるページを掲載しています．
自力でいけるところまで頑張ってみてください．
困ったとき・完成したときは遠慮なく近くのCore-team Memberまで！

## まずはローカル環境でMQTTを試す

ヒント：Mosquito

参考：https://tech-and-investment.com/raspberrypi-picow-6-mqtt/

> [!NOTE]
> デフォルトのMosquittoは外部との通信ができないため、`mosquitto.conf` を編集して外部からの接続を許可する必要があります。
>
> `mosquitto -c mosquitto.conf` で設定ファイルを指定して起動します。
>
> 参考：https://qiita.com/vfuji/items/6d01e9f613b92d638574#%E6%BA%96%E5%82%99%E4%BD%9C%E6%A5%AD
> [!NOTE]
> Pico WにMosquittoを扱うためのライブラリ`umqtt.simple`をインストールする必要がありますが，「パッケージを管理」で検索する際，`umqtt`で検索してもヒットしないため，`umqtt.simple`と検索するようにしましょう．
##  Microsoft Azure IoT Hubで時系列データを見る

参考
- [macOS での Azure CLI のインストール](https://learn.microsoft.com/ja-jp/cli/azure/install-azure-cli-macos)
- [Azure IoT Hub に Mosquitto™ から MQTT なげてみる](https://qiita.com/narutaro/items/1a16ff1321f5044afaf0)


[目次に戻る](README.md)
