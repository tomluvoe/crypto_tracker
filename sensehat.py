#!/bin/python3

from crypto_tracker import CryptoTracker
from sense_hat import SenseHat
import time
import re

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

ct = CryptoTracker()
sense = SenseHat()
start = time.time()
ct.refresh()

while 1:
    if time.time() - start > 60:
        ct.refresh()
        start = time.time()
    for coin in ct.get_result(list=True):
        fg_color = blue
        bg_color = black
        ma = re.search('([-+]?\d*\.\d+)%', coin)
        if ma:
            fg_color = green if float(ma.group(1)) > 0 else red
        sense.show_message(coin, fg_color, bg_color)
