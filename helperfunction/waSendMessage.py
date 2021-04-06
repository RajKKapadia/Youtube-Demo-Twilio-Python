import os

from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM = os.environ.get('FROM')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):

    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}'
    )
    return res
