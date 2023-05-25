from mailing.logic.perform_mailing.model import MessagingService


class FakeSender(MessagingService):
    def send(self, target, message) -> str:
        return 'OK'
