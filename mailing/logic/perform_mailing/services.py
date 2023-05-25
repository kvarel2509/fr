from collections import deque

from .model import FailedSend, is_mailing_end_date_come, is_time_of_client_in_valid_mailing_time_interval


class MailingPerformer:
    def __init__(self, mailing_repo, client_repo, messaging_service):
        self.mailing_repo = mailing_repo
        self.client_repo = client_repo
        self.messaging_service = messaging_service

    def run_mailing(self, mailing_id):
        mailing = self.mailing_repo.mailing_by_id(mailing_id)
        clients = deque(self.client_repo.filter_clients(**mailing.filters))

        while clients:
            if mailing.end_date and is_mailing_end_date_come(mailing.end_date):
                break
            client = clients.popleft()
            if is_time_of_client_in_valid_mailing_time_interval(
                mailing.time_interval_start, mailing.time_interval_end, client.time_zone
            ):
                try:
                    status = self.messaging_service.send(client.phone, mailing.message)
                    self.mailing_repo.create_message(status=status, mailing=mailing, client=client)
                except FailedSend:
                    clients.append(client)
