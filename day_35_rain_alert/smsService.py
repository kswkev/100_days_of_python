#twilio recovery code = M8H7GQK8BZW5T3K2QAL215WD
from twilio.rest import Client
import os

class SmsService:

    def __init__(self):
        self.SENDING_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
        self.SID = os.getenv("TWILIO_SID")
        self.AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self.SID, self.AUTH_TOKEN)

    def send_message(self, recipient_number, message):
        message = self.client.messages.create(from_=self.SENDING_PHONE_NUMBER, to=recipient_number, body=message)
        print(message.status)