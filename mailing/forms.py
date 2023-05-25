from django import forms

from .models import Mailing
from .validators import MailingValidator


class MailingForm(forms.ModelForm):
    filters = forms.JSONField(required=False, initial=dict)

    validator = MailingValidator()

    class Meta:
        model = Mailing
        fields = ('start_date', 'message', 'filters', 'end_date', 'time_interval_start', 'time_interval_end')
        labels = {
            'start_date': 'Дата начала исполнения',
            'message': 'Сообщение',
            'filters': 'Условия выборки клиентов',
            'end_date': 'Дата окончания рассылки',
            'time_interval_start': 'Начало временного интервала',
            'time_interval_end': 'Конец временного интервала'
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        self.validator.validate_start_date(start_date)
        return start_date

    def clean_message(self):
        message = self.cleaned_data.get('message')
        self.validator.validate_message(message)
        return message

    def clean_filters(self):
        filters = self.cleaned_data.get('filters')
        self.validator.validate_filters(filters)
        return filters

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        self.validator.validate_end_date(end_date)
        return end_date

    def clean_time_interval_start(self):
        time_interval_start = self.cleaned_data.get('time_interval_start')
        self.validator.validate_time_interval_start(time_interval_start)
        return time_interval_start

    def clean_time_interval_end(self):
        time_interval_end = self.cleaned_data.get('time_interval_end')
        self.validator.validate_time_interval_end(time_interval_end)
        return time_interval_end

    def clean(self):
        self.validator.validate(**self.cleaned_data)
        return super().clean()
