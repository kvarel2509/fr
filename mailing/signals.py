from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .logic.mailing_tasks import create_task, replace_task, delete_task
from .models import Mailing
from .repository import MailingRepository


@receiver(post_save, sender=Mailing)
def assign_task(sender, instance, **kwargs):
    repo = MailingRepository()
    task_id = create_task(instance) if kwargs['created'] else replace_task(instance)
    repo.create_mailing_task(instance, task_id)


@receiver(pre_delete, sender=Mailing)
def cancel_task(sender, instance, **kwargs):
    delete_task(instance)
