import paho.mqtt.client as mqtt
import threading
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# Данные WebClient mqtt HiveMq
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
broker_address = os.getenv("BROKER")  # mqtt брокер
port = int(os.getenv("PORT"))  # порт для MQTT

def on_connect(client, userdata, flags, rc):
    """Callback-функция для обработки события подключения к брокеру"""
    if rc == 0:
        print("Connected")
    else:
        print(f"Couldn't connect: {rc}")


def on_message(client, userdata, msg):
    """Callback-функция для обработки получения нового сообщения"""
    if msg.topic == "target":
        client.publish("ping", "recieved") # Подтверждение принятия

        match int(msg.payload.decode('utf-8')):
            case 1: os.system("shutdown /s") # Выключение
            case 2: os.system("shutdown /h") # Сон
            case 3: os.system("shutdown /r") # Перезагрузка
            case 4: os.system("Rundll32.exe user32.dll,LockWorkStation") # Блокировка

def on_disconnect(client, userdata, rc):
    """Переподключение к брокеру при разрыве соединения"""
    started = True
    while started:
        try:
            client.reconnect()
            started = False
        except:
            started = True
            print("An error has occurred, reboot in 10 seconds")
            time.sleep(10)
            print("rebooting...")

# Создание клиента MQTT
client = mqtt.Client()

# Установка имени пользователя и пароля
client.username_pw_set(username, password)

# Назначение callback-функций
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Подключение к брокеру
started = True
while started:
    try:
        client.connect(broker_address, port, keepalive=60)
        started = False
    except:
        started = True
        print("An error has occurred, reboot in 10 seconds")
        time.sleep(10)
        print("rebooting...")

# Подписка на топик
client.subscribe("target")

def main_loop():
    """Цикл во втором потоке; Отправляем каждые 5 секунд текущее время для статуса онлайна в приложении"""
    while True:
        client.subscribe("target")
        client.publish("ping", 0)
        time.sleep(5)

if __name__ == '__main__':
    """Точка входа"""
    # Создание и запуск потока
    thread = threading.Thread(target=main_loop)
    thread.start()

    # Основной цикл MQTT клиента
    client.loop_forever()
