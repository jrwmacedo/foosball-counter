import time

from boot import station, ssid, password, PIN_PLUS_TEAM_1, \
    PIN_PLUS_TEAM_2, connecting_interval_reset_counter
from button import setupButtons, team_1, team_2, plusButtonManagement, minusButtonManagement, resetCounterManagement, \
    checkMQQTMode
from connection import connect_and_subscribe, client
from sensor import Sensor

sensor_1 = Sensor(PIN_PLUS_TEAM_1)
sensor_2 = Sensor(PIN_PLUS_TEAM_2)

try:
    team_1.display.startDisplay()
    team_2.display.startDisplay()
    setupButtons()
    checkMQQTMode(client)
    if client.MQTTMode:
        station.active(True)
        station.connect(ssid, password)
        timeout = time.time()
        while not station.isconnected() and (time.time() - timeout) < connecting_interval_reset_counter:
            pass
            print('The timeout is' + str(time.time() - timeout))
        print('Connection successful')
        print(station.ifconfig())

        connect_and_subscribe()
        team_1.display.tm.show('OLN ')
        team_2.display.tm.show('OLN ')
        time.sleep(3)

except OSError as e:
    print('Exception:' + str(e))
    checkMQQTMode(client, True)

resetCounterManagement(client, team_1, team_2, True)

while True:
    try:
        client.check_msg()
        plusButtonManagement(client, team_1)
        plusButtonManagement(client, team_2)
        minusButtonManagement(client, team_1)
        minusButtonManagement(client, team_2)
        resetCounterManagement(client, team_1, team_2)
    except OSError as e:
        checkMQQTMode(client, True)
        team_1.display.tm.number(team_1.counter)
        team_2.display.tm.number(team_2.counter)
