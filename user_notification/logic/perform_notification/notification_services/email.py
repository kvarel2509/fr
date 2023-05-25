from django.core.mail import EmailMessage

from ..base_model import NotificationService


class EmailNotificator(NotificationService):
    def __init__(self, subject):
        self.subject = subject

    def notify(self, target, message):
        email = EmailMessage(subject=self.subject, body=message, to=[target])
        email.send()
