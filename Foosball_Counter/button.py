import time

import machine

from boot import PIN_PLUS_TEAM_1, PIN_PLUS_TEAM_2, PIN_MINUS_TEAM_2, PIN_MINUS_TEAM_1, \
    PIN_CLK_DISPLAY_TEAM_2, PIN_DIO_DISPLAY_TEAM_2, PIN_DIO_DISPLAY_TEAM_1, \
    PIN_CLK_DISPLAY_TEAM_1
from counter import Counter
from display import Display
from message import checkMessageToSend

display_1 = Display(PIN_CLK_DISPLAY_TEAM_1, PIN_DIO_DISPLAY_TEAM_1, 'T-01')
display_2 = Display(PIN_CLK_DISPLAY_TEAM_2, PIN_DIO_DISPLAY_TEAM_2, 'T-02')

team_1 = Counter("Team 1", display_1)
team_2 = Counter("Team 2", display_2)


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
        team.display.tm.number(team.counter)
        team.buttonPlusPressing = 1
        time.sleep(1)
    elif team.buttonPlusPressing and team.buttonPlus.value():
        print('Button released!')
        team.buttonPlusPressing = 0
    checkMessageToSend(client, team)


def minusButtonManagement(client, team: Counter):
    if not team.buttonMinusPressing and not team.buttonMinus.value() and team.counter > 0:
        print('Button Minus pressed!')
        team.counter -= 1
        team.display.tm.number(team.counter)
        team.buttonMinusPressing = 1
    elif team.buttonMinusPressing and team.buttonMinus.value():
        print('Button Minus released!')
        team.buttonMinusPressing = 0
    checkMessageToSend(client, team)


def resetCounterManagement(client, team1: Counter, team2: Counter, force: bool = False):
    while (team1.buttonPlusPressing and team2.buttonPlusPressing
           and not team1.counter == 0 and not team2.counter == 0) or force:
        force = False
        print('Reset counter')
        resetCounter(client, team_1)
        resetCounter(client, team_2)


def resetCounter(client, team: Counter):
    team.counter = 0
    team.display.tm.number(team.counter)
    checkMessageToSend(client, team)


def checkMQQTMode(client, forcelocal: bool = False):
    if (not team_1.buttonMinus.value() and not team_2.buttonMinus.value()) or forcelocal:
        client.MQTTMode = False
        print('MQTT Mode disabled!')
        print('Working locally...')
        team_1.display.tm.show('LOC ')
        team_2.display.tm.show('LOC ')
        time.sleep(3)
