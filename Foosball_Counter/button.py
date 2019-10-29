import time
from boot import PIN_PLUS_TEAM_1, PIN_PLUS_TEAM_2, PIN_MINUS_TEAM_2, PIN_MINUS_TEAM_1, pressing_interval_reset_counter
from counter import Counter
from message import checkMessageToSend
import machine

team_1 = Counter("Team 1")
team_2 = Counter("Team 2")


def setupButtons():
    print('Configuring buttons...')
    team_1.buttonPlus = machine.Pin(PIN_PLUS_TEAM_1, machine.Pin.IN, machine.Pin.PULL_UP)
    team_2.buttonPlus = machine.Pin(PIN_PLUS_TEAM_2, machine.Pin.IN, machine.Pin.PULL_UP)
    team_1.buttonMinus = machine.Pin(PIN_MINUS_TEAM_1, machine.Pin.IN, machine.Pin.PULL_UP)
    team_2.buttonMinus = machine.Pin(PIN_MINUS_TEAM_2, machine.Pin.IN, machine.Pin.PULL_UP)
    print('Buttons configured!')


def plusButtonManagement(client, team: Counter):
    if not team.buttonPlusPressing and not team.buttonPlus.value():
        print('Button pressed!')
        team.counter += 1
        team.buttonPlusPressing = 1
    elif team.buttonPlusPressing and team.buttonPlus.value():
        print('Button released!')
        team.buttonPlusPressing = 0
    checkMessageToSend(client, team)


def minusButtonManagement(client, team: Counter):
    if not team.buttonMinusPressing and not team.buttonMinus.value() and team.counter > 0:
        print('Button Minus pressed!')
        team.counter -= 1
        team.buttonMinusPressing = 1
    elif team.buttonMinusPressing and team.buttonMinus.value():
        print('Button Minus released!')
        team.buttonMinusPressing = 0
    checkMessageToSend(client, team)


def resetCounterManagement(client, team1: Counter, team2: Counter):
    storedtime = time.time()
    while team1.buttonPlusPressing and team2.buttonPlusPressing and not team1.counter == 0 and not team2.counter == 0:
        if (time.time() - storedtime) > pressing_interval_reset_counter:
            print('Reset counter')
            team1.counter = 0
            team2.counter = 0
            checkMessageToSend(client, team1)
            checkMessageToSend(client, team2)


def checkMQQTMode(client):
    if not team_1.buttonMinus.value() and not team_2.buttonMinus.value():
        client.MQTTMode = False
        print('MQTT Mode disabled!')
