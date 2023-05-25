import datetime

from celery import shared_task

from mailing.repository import MailingRepository
from .logic.perform_notification.daily_mailing_report.services import DailyMailingReportPerformer
from .logic.perform_notification.notification_services.email import EmailNotificator
from .repository import NotificationRepository


@shared_task
def send_daily_mailing_report():
    notification_repo = NotificationRepository()
    mailing_repo = MailingRepository()
    date = datetime.date.today()
    notification_service = EmailNotificator(f'Отчет за {date.isoformat()}')
    performer = DailyMailingReportPerformer(notification_repo, mailing_repo, notification_service, date)
    performer.run_notification('daily_mailing_report')
