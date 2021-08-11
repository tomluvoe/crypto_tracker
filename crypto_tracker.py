#!/bin/python3

import requests

class CryptoTracker:

    def __init__(self, coins = 'bitcoin,ethereum,cardano'):
        self.coins = coins
        self.url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coins}'
        self.success = False
        self.date = ''
        self.crypto_string = ''
        self.crypto_list = []

    def refresh(self):
        try:
            response = requests.get(self.url)
        except:
            self.success = False
            return False
        if (response.status_code == 200):
            self.success = True
            self.date = response.json()[0]['last_updated'].replace('T', ' ')
            self.crypto_string = ''
            self.crypto_list = [self.date]
            for resp in response.json():
                sym = resp['symbol'].upper()
                pct = f"{round(resp['price_change_percentage_24h'],1)}%"
                price = f"${resp['current_price']}"
                ct_str = f"{sym} {price} {pct}  "
                self.crypto_string += ct_str
                self.crypto_list.append(ct_str)
            return True
        else:
            self.success = False
            return False

    def get_result(self, list=False):
        if list:
            return self.crypto_list
        return f"{self.date}  {self.crypto_string}"
