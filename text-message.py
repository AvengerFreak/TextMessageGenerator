import os
from etext import send_sms_via_email
from dotenv import load_dotenv

load_dotenv()

phone_number = os.getenv('RECIPIENT_PHONE_NUMBER') # number of person you want to send message
sender = os.getenv('SENDER_EMAIL') # gmail you used to generate app password
password = os.getenv('EMAIL_PASSWORD') # generate app password in gmail account
message = "I Love You - by code!"
subject = "Python Generated Text"
provider = "T-Mobile"

sender_credentials = (sender, password)

send_sms_via_email(
    phone_number, message, provider, sender_credentials, subject=subject
)


