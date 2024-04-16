# 2. LINE Notify を利用した簡易Botの開発

## LINE Notify アクセストークンの取得

### 1. LINE Notify にログイン

[LINE Notify](https://notify-bot.line.me/ja/) にアクセスし、右上のボタンからログインします。

ログイン後、右上の自分の名前をクリックし、`マイページ` を選択します。

### 2. LINE Notify トークンの取得

`アクセストークンの発行(開発者向け)` から `トークンを発行する` を選択します。

好きなトークン名を入力し、トークルームは `1:1でLINE Notifyから通知を受け取る` を選択し、`発行する` をクリックします。

トークンが発行されるので、コピーしておきます。

> [!CAUTION]
> トークンは他人に知られないように注意してください。

> [!TIP]
> トークンの再発行はできないため、ブラウザのタブを開いたままにしておくと便利です。
>
> タブを閉じてしまった場合は、古いトークンを削除して新しいトークンを発行しましょう。

## 本体温度センサを利用した通知デモ

1章で作成したコードをベースに、まずは文字列をLINEで送ってみましょう。

```python
...
import urequests

# SSID, password, LINE Notify Token, 通知メッセージを設定してください
ssid = "ssid"
password = "password"
token = "token"
message = "hello, Raspberry Pi"


def connect():
    ...


def send_line(token, message):
    # LINE Notify APIを使ってメッセージを送信
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "message=" + message
    response = urequests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Failed to send notification, status code:", response.status_code)
    response.close()


try:
    ip = connect()
    while True:
        if rp2.bootsel_button() == 1:
            # LEDが光っている間はLINE送信中
            machine.Pin("LED", machine.Pin.OUT).on()
            send_line(token, message)
            machine.Pin("LED", machine.Pin.OUT).off()
except KeyboardInterrupt:
    machine.reset()
```

## (Optional) GPIOを利用した温度監視システムの構築



[目次に戻る](README.md)
