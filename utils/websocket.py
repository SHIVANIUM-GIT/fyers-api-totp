from fyers_api.websocket import ws
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NzMyOTIzNTUsImV4cCI6MTY3MzMxMDY1NSwibmJmIjoxNjczMjkyMzU1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCanZHcER1U0U5U09JM0syelE1eG1QYmZjZEdzQWNkekxlSVpzZjNObHpnNFprZm1aZmdRY0lzSmhHZFlaSVN3eUU5aW8tZ0R1WnJGY0Z3NlVHUHJKN3lNQ1hCd1ZNdUdWNnBCYkVlYUc2bEtzOFVWZz0iLCJkaXNwbGF5X25hbWUiOiJTSElWIEtVTUFSIFJBVEhPUkUiLCJvbXMiOm51bGwsImZ5X2lkIjoiWFMxMjE0MSIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.cumZ0FrVLfDPJmNsxblBJyhD_aoWC8N7YqEyFtSPTBs"

access_token = client_id+':'+token
data_type='symbolData'
symbol=['NSE:TATAMOTORS-EQ']

def custom_message(ticks):
    print(dir(ticks))
    
ws.FyersSocket.websocket_data=custom_message
fs = ws.FyersSocket(access_token, data_type, symbol)
fs.subscribe()