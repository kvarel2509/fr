from django.db.models import Count

from .models import Mailing, Message, MailingTask
from .validators import MailingValidator


class MailingRepository:
    def __init__(self, validator=MailingValidator()):
        self.validator = validator

    def all_mailings(self):
        return Mailing.objects.all()

    def mailing_by_id(self, mailing_id):
        return Mailing.objects.get(pk=mailing_id)

    def create_mailing(self, start_date, message, filters, time_interval_start, time_interval_end, end_date=None):
        self.validator.validate_start_date(start_date)
        self.validator.validate_message(message)
        self.validator.validate_filters(filters)
        self.validator.validate_end_date(end_date)
        self.validator.validate_time_interval_start(time_interval_start)
        self.validator.validate_time_interval_end(time_interval_end)
        self.validator.validate(
            start_date=start_date,
            message=message,
            filters=filters,
            time_interval_start=time_interval_start,
            time_interval_end=time_interval_end,
            end_date=end_date
        )
        mailing = Mailing(
            start_date=start_date,
            message=message,
            filters=filters,
            time_interval_start=time_interval_start,
            time_interval_end=time_interval_end,
            end_date=end_date
        )
        mailing.save()
        return mailing

    def create_message(self, status, mailing, client):
        message = Message(status=status, mailing=mailing, client=client)
        message.save()
        return message

    def get_message_groups_by_status(self, mailing_id=None):
        query = Message.objects.all()
        if mailing_id:
            query = query.filter(mailing_id=mailing_id)
        query = query.values('status').annotate(message_count=Count('status'))
        return query

    def get_message_groups_by_status_in_date_range(self, start_date_interval=None, end_date_interval=None):
        query = Message.objects.all()
        if start_date_interval:
            query = query.filter(create_date__gte=start_date_interval)
        if end_date_interval:
            query = query.filter(create_date__lte=end_date_interval)
        query = query.values('status').annotate(message_count=Count('status'))
        return query

    def create_mailing_task(self, mailing, task_id):
        task = MailingTask(mailing=mailing, task=task_id)
        task.save()
        return task
