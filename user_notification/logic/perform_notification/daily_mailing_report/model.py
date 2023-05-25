import datetime
from django.utils import timezone


def get_start_datetime_for_date(date):
    return datetime.datetime.combine(
        date,
        datetime.time.min,
        timezone.get_current_timezone()
    )


def get_end_datetime_for_date(date):
    return datetime.datetime.combine(
        date,
        datetime.time.max,
        timezone.get_current_timezone()
    )
