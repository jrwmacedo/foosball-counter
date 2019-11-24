import time

import machine

from boot import client_id, mqtt_server, topic_sub
from button import team_1, team_2
from message import checkMessageToSend
from umqttsimple import MQTTClient

client = MQTTClient(client_id, mqtt_server)


def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification':
        if msg == b'received':
            print('ESP received hello message')
        elif 'connected' in str(msg):
            devicemessage = str(msg).split(':')
            print(devicemessage[1])
            checkMessageToSend(client, team_1, True)
            checkMessageToSend(client, team_2, True)


def connect_and_subscribe():
    if client.MQTTMode:
        client.set_callback(sub_cb)
        client.connect()
        client.subscribe(topic_sub)
        print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
        return client


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
