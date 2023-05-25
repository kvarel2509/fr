import requests

from mailing.logic.perform_mailing.model import MessagingService, FailedSend


class FBRQSender(MessagingService):
    URL = 'https://probe.fbrq.cloud/v1/send/0'

    def __init__(self, token):
        self.token = token

    def send(self, target, message) -> str:
        body = {
            "id": 0,
            "phone": int(target),
            "text": message
        }
        try:
            response = requests.post(self.URL, headers={'Authorization': self.token}, json=body, timeout=10)
            if response.status_code == requests.codes.ok:
                json = response.json()
                return json.get('message', 'invalid status')
            else:
                raise requests.HTTPError()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError):
            raise FailedSend()
