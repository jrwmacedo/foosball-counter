from boot import PIN_SENSOR_TEAM_1, PIN_SENSOR_TEAM_2, station, ssid, password
from button import setupButtons, team_1, team_2, plusButtonManagement, minusButtonManagement, resetCounterManagement, \
    checkMQQTMode
from connection import connect_and_subscribe, restart_and_reconnect, client
from sensor import Sensor

sensor_1 = Sensor(PIN_SENSOR_TEAM_1)
sensor_2 = Sensor(PIN_SENSOR_TEAM_2)
try:
    setupButtons()
    checkMQQTMode(client)
    if client.MQTTMode:
        station.active(True)
        station.connect(ssid, password)

        while not station.isconnected():
            pass

        print('Connection successful')
        print(station.ifconfig())

        connect_and_subscribe()
    else:
        print('Working locally...')


except OSError as e:
    print('Exception:' + str(e))
    restart_and_reconnect()

while True:
    try:
        sensor_1.presenceDetected(client, team_1)
        sensor_2.presenceDetected(client, team_2)
        client.check_msg()
        plusButtonManagement(client, team_1)
        plusButtonManagement(client, team_2)
        minusButtonManagement(client, team_1)
        minusButtonManagement(client, team_2)
        resetCounterManagement(client, team_1, team_2)
    except OSError as e:
        restart_and_reconnect()
