import binascii

import machine
import network

ssid = ''
password = ''
mqtt_server = '192.168.1.1'
client_id = binascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'counter'
MQTTMode = True
connecting_interval_reset_counter = 5
PIN_PLUS_TEAM_1 = 14
PIN_PLUS_TEAM_2 = 3
PIN_MINUS_TEAM_1 = 4
PIN_MINUS_TEAM_2 = 5

PIN_CLK_DISPLAY_TEAM_1 = 13
PIN_DIO_DISPLAY_TEAM_1 = 0

PIN_DIO_DISPLAY_TEAM_2 = 2
PIN_CLK_DISPLAY_TEAM_2 = 12

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)
