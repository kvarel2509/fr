from mailing.forms import MailingForm as BaseMailingFrom
from .widgets import DateTimeWidget, TimeWidget


class MailingFrom(BaseMailingFrom):
    class Meta(BaseMailingFrom.Meta):
        widgets = {
            'start_date': DateTimeWidget(),
            'end_date': DateTimeWidget(),
            'time_interval_start': TimeWidget(),
            'time_interval_end': TimeWidget()
        }
