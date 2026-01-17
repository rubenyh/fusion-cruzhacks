import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
Account_SID = os.getenv('Account_SID')
Auth_Token = os.getenv('Auth_Token')
phone_number = os.getenv('phone_number')

client = Client(Account_SID, Auth_Token)
def sendSms(to:str, body:str):
    message = client.messages.create(
            to=to,
            from_=phone_number,
            body=body
    )
    return {
        "status": "successfully",
        "message_sid": message.sid,
        "to": message.to,
        "from": message.from_,
        "twilio_status": message.status
    }
