from celery import shared_task
from django.conf import settings

from clients.repository import ClientRepository
from .logic.perform_mailing.messaging_services.fbrq import FBRQSender
from .logic.perform_mailing.services import MailingPerformer
from .repository import MailingRepository


@shared_task
def perform_mailing(mailing_id):
    mailing_repo = MailingRepository()
    client_repo = ClientRepository()
    messaging_service = FBRQSender(settings.FBRQ_TOKEN)
    mailing_performer = MailingPerformer(mailing_repo, client_repo, messaging_service)
    mailing_performer.run_mailing(mailing_id)
