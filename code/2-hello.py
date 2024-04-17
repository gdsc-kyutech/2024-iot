import network
from time import sleep
import machine
import urequests

ssid = "KIT-EVENT"
password = "password"
token = "token"
message = "hello, Raspberry Pi"


def connect():
    # Wi-Fiに接続
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip


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
