from abc import ABC, abstractmethod
from zoneinfo import ZoneInfo

from django.utils import timezone


class FailedSend(Exception):
    pass


class MessagingService(ABC):
    @abstractmethod
    def send(self, target, message) -> str: ...


def is_mailing_end_date_come(end_date):
    return timezone.now() > end_date


def is_time_of_client_in_valid_mailing_time_interval(time_interval_start, time_interval_end, time_zone):
    client_time = timezone.localtime(timezone=ZoneInfo(time_zone)).time()
    if time_interval_start < time_interval_end:
        return time_interval_start < client_time < time_interval_end
    else:
        return time_interval_start < client_time or client_time < time_interval_end
