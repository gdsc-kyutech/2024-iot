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

##  Microsoft Azure IoT Hubで時系列データを見る  

参考： https://qiita.com/narutaro/items/1a16ff1321f5044afaf0

[4-(b) 他のボードやセンサ，ディスプレイなどを試してみる](4-other.md) へ進む

[目次に戻る](README.md)