from django.db import models

from clients.models import Client
from .constants import DAY_START_TIME, DAY_END_TIME


class Mailing(models.Model):
    start_date = models.DateTimeField()
    message = models.TextField()
    filters = models.JSONField(default=dict)
    end_date = models.DateTimeField(null=True, blank=True)
    time_interval_start = models.TimeField(default=DAY_START_TIME)
    time_interval_end = models.TimeField(default=DAY_END_TIME)

    class Meta:
        db_table = 'mailing'
        indexes = [
            models.Index(fields=['start_date'])
        ]


class MailingTask(models.Model):
    mailing = models.OneToOneField(Mailing, on_delete=models.CASCADE, related_name='mailing_task', primary_key=True)
    task = models.CharField(max_length=255)

    class Meta:
        db_table = 'mailing_task'


class Message(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        db_table = 'message'
        indexes = [
            models.Index(fields=['status'])
        ]
