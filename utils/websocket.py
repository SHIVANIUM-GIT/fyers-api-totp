from fyers_api.websocket import ws
import os
import time
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
token = os.getenv("ACCESS_TOKEN")

access_token = client_id + ":" + token
data_type = "symbolData"
symbol = ["NSE:TATAMOTORS-EQ"]


def custom_message(ticks):
    print("HELLO")
    print(dir(ticks))


ws.FyersSocket.websocket_data = custom_message
fs = ws.FyersSocket(access_token, data_type, symbol)
fs.subscribe()
time.sleep(180)
fs.unsubscribe()
