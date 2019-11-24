import time

from machine import Pin

import tm1637


class Display:
    def __init__(self, clockpin, diopin, initmessage):
        self.tm = tm1637.TM1637(clk=Pin(clockpin), dio=Pin(diopin))
        self.initmessage = initmessage

    def startDisplay(self):
        self.tm.show(self.initmessage)
        time.sleep(3)
        self.tm.show('W8  ')
