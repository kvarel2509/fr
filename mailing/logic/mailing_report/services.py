class MailingReporter:
    def __init__(self, mailing_repo):
        self.mailing_repo = mailing_repo

    def get_report(self, mailing_id):
        mailing_report = self.mailing_repo.get_message_groups_by_status(mailing_id)
        return mailing_report
