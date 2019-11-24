import time
import tm1637
from machine import Pin


class Display:
    def __init__(self, clockpin, diopin, initmessage):
        self.tm = tm1637.TM1637(clk=Pin(clockpin), dio=Pin(diopin))
        self.initmessage = initmessage

    def startDisplay(self):
        self.tm.show(self.initmessage)
        time.sleep(3)
        self.tm.number(0)
