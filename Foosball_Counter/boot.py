import binascii
import machine
import network

ssid = ''
password = ''
mqtt_server = ''
client_id = binascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'counter'
MQTTMode = True
pressing_interval_reset_counter = 2
PIN_PLUS_TEAM_1 = 12
PIN_PLUS_TEAM_2 = 14
PIN_MINUS_TEAM_1 = 4
PIN_MINUS_TEAM_2 = 5

PIN_SENSOR_TEAM_1 = 13
PIN_SENSOR_TEAM_2 = 0

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)
