import json
import requests
import time

from boltiot import Bolt
import Conf

mybolt = Bolt(Conf.API_KEY, Conf.DEVICE_ID)

sell_price = 7000

def get_bitcoin_price():
    URL = "https://min-api.crytocompare.com/data/price?fsym=bTC&tsyms=USD"
    response = requests.request("GET", URL)
    response = json.loads(response.text)
    current_price = response["USD"]
    return current_price


while True:
    current_price = get_bitcoin_price()
    print("The current price is: ", current_price)

    if current_price > sell_price:
        print(" ALERT: current price has exceeded the selling price")
        response = mybolt.digitalWrite( '0','HIGH' )
        print( response )
    time.sleep(5)
    response = mybolt.digitalWrite( '0','LOW')

    time.sleep(10)
