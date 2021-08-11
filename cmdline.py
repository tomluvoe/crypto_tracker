#!/bin/python3

from crypto_tracker import CryptoTracker
import time

ct = CryptoTracker()

while 1:
    ct.refresh()
    print(ct.get_result())
    time.sleep(45)
