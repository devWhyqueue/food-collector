import os

from twilio.rest import Client


def build_message(updated_threads):
    msg = f'Hi,\nthere are new posts regarding intro collections!\nThese threads have new posts:\n'
    for thread in updated_threads:
        msg += f'- {thread}\n'
    msg += '\nGo get the food,\nThe Food Collector'
    return msg


class SMSNotifier:
    def __init__(self, receiver):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self._client = Client(account_sid, auth_token)
        self._sender_number = os.environ['TWILIO_PHONE']
        self._receiver = receiver

    def send_message(self, message):
        self._client.messages.create(from_=self._sender_number, body=message, to=self._receiver)
