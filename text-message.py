import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
print("getting credentials from .env")
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

"""
curl.exe -X POST "https://api.twilio.com/2010-04-01/Accounts/sid/Messages.json" ^
  --data-urlencode "Body=message" ^
  --data-urlencode "From=sender" ^
  --data-urlencode "To=recipient" ^
  -u "sid:auth-token"
"""

print("sending message")
message = client.messages \
    .create(
         body=os.getenv('SECRET_MESSAGE'),
         from_=os.getenv('SENDER_PHONE_NUMBER'),
         to= os.getenv('RECIPIENT_PHONE_NUMBER')
     )

print("message was sent sucessfully")



