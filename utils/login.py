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

# response = session.generate_authcode()
# print(response)

auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzM1NDYwNzEsImV4cCI6MTY3MzU3NjA3MSwibmJmIjoxNjczNTQ1NDcxLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzEyMTQxIiwib21zIjpudWxsLCJub25jZSI6IiIsImFwcF9pZCI6IkJHR1NNRjJZUUoiLCJ1dWlkIjoiMGVkZWEzYTMyYjYzNDI1Yjk3YmEwN2ExM2UxYTg3ZjkiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.y6THZZn2lWRaoz90n8BX5XgBrSpE4B1FJnB_iNOAO4Q"
session.set_token(auth_code)
response = session.generate_token()

access_token = response["access_token"]
print("ACCESS TOKEN : ", access_token)

# Check your holdings
fyers = fyersModel.FyersModel(client_id=client_id, token=os.getenv("ACCESS_TOKEN"))
print(fyers.holdings())
