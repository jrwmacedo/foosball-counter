import time

from machine import Pin

from counter import Counter
from message import checkMessageToSend


class Sensor:

    def __init__(self, sensorpin):
        self.pir = Pin(sensorpin, Pin.IN)
        self.messageSent = 0
        self.sensorpin = sensorpin
        self.detecting = 0

    def presenceDetected(self, client, team: Counter):
        if not self.pir.value():
            if not self.messageSent:
                team.counter += 1
                print('Motion detected!' + str(self.sensorpin))
                checkMessageToSend(client, team)
                self.messageSent = 1
                time.sleep(2)
        else:
            self.messageSent = 0
