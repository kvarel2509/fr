from celery.result import AsyncResult

from ..tasks import perform_mailing


def create_task(mailing):
    result = perform_mailing.apply_async(args=(mailing.id,), eta=mailing.start_date)
    task_id = result.task_id
    return task_id


def delete_task(mailing):
    task_id = mailing.mailing_task.task
    AsyncResult(task_id).revoke()


def replace_task(mailing):
    delete_task(mailing)
    return create_task(mailing)
