from .model import get_start_datetime_for_date, get_end_datetime_for_date
from ..base_services import NotificationPerformer


class DailyMailingReportPerformer(NotificationPerformer):
    def __init__(self, notification_repo, mailing_repo, notification_service, date):
        self.notification_repo = notification_repo
        self.mailing_repo = mailing_repo
        self.notification_service = notification_service
        self.date = date

    def get_contacts(self, subscription_name):
        subscription = self.notification_repo.get_subscription_by_name(subscription_name)
        users = self.notification_repo.get_subscribed_users(subscription)
        emails = [user.email for user in users]
        return emails

    def get_data(self):
        start_date = get_start_datetime_for_date(self.date)
        end_date = get_end_datetime_for_date(self.date)
        data = self.mailing_repo.get_message_groups_by_status_in_date_range(start_date, end_date)
        return data

    def notify(self, contact, text):
        self.notification_service.notify(contact, text)

    def format(self, data):
        return '\n'.join([f"{item.get('status')} - {item.get('message_count')}" for item in data])
