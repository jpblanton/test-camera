import time
import io

import picamera
import paho.mqtt.client as mqtt
from decouple import config

topic = config('PUB_TOPIC')
host = config('MQTT_HOST')
port = config('MQTT_PORT', cast=int)

def on_connect(client, userdata, flags, rc):
    client.subscribe(config('SUB_TOPIC'))


client = mqtt.Client()
client.on_connect = on_connect

client.connect(host, port, 60)

client.loop_start()

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)

    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, 'jpeg'):
        stream.seek(0)
        client.publish(topic, payload=stream.getvalue(), retain=True)
        stream.seek(0)
        stream.truncate()
        time.sleep(30)
