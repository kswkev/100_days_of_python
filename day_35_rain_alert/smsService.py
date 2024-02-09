#twilio recovery code = M8H7GQK8BZW5T3K2QAL215WD
from twilio.rest import Client

SENDING_PHONE_NUMBER = "+447488897864"
SID = "ACc27108cebc24480527cd5b424f44c49a"
AUTH_TOKEN = "b90511728fbb0f329851e39ebdba96a5"

class SmsService:

    def __init__(self):
        self.client = Client(SID, AUTH_TOKEN)

    def send_message(self, recipient_number, message):
        message = self.client.messages.create(from_=SENDING_PHONE_NUMBER, to=recipient_number, body=message)
        print(message.status)