from fyers_api import accessToken
from fyers_api import fyersModel
from fyers_api.websocket import ws
import sys
from dotenv import load_dotenv
import time
import os

load_dotenv()


client_id = os.getenv("CLIENT_ID")
secret_key = os.getenv("SECRET_KEY")
redirect_url = "http://127.0.0.1/login"

session = accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_url,
    response_type="code",
    grant_type="authorization_code",
)

response = session.generate_authcode()
# print(response)

# session.set_token(auth_code)
# response = session.generate_token()

# access_token = response["access_token"]
# print(access_token)
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NzMyOTIzNTUsImV4cCI6MTY3MzMxMDY1NSwibmJmIjoxNjczMjkyMzU1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCanZHcER1U0U5U09JM0syelE1eG1QYmZjZEdzQWNkekxlSVpzZjNObHpnNFprZm1aZmdRY0lzSmhHZFlaSVN3eUU5aW8tZ0R1WnJGY0Z3NlVHUHJKN3lNQ1hCd1ZNdUdWNnBCYkVlYUc2bEtzOFVWZz0iLCJkaXNwbGF5X25hbWUiOiJTSElWIEtVTUFSIFJBVEhPUkUiLCJvbXMiOm51bGwsImZ5X2lkIjoiWFMxMjE0MSIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.cumZ0FrVLfDPJmNsxblBJyhD_aoWC8N7YqEyFtSPTBs
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
print(fyers.holdings())
