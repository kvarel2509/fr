from django import forms

from .models import Client
from .validators import ClientValidator


class ClientAdminForm(forms.ModelForm):
    validator = ClientValidator()

    class Meta:
        model = Client
        fields = ('phone', 'mobile_operator_code', 'tag', 'time_zone')
        labels = {
            'phone': 'Телефон',
            'mobile_operator_code': 'Код мобильного оператора',
            'tag': 'Тег',
            'time_zone': 'Часовой пояс'
        }
        help_texts = {
            'phone': '7xxxxxxxxxx (10 зн.)',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        self.validator.validate_phone(phone)
        return phone

    def clean_mobile_operator_code(self):
        mobile_operator_code = self.cleaned_data.get('mobile_operator_code')
        self.validator.validate_mobile_operator_code(mobile_operator_code)
        return mobile_operator_code

    def clean_tag(self):
        tag = self.cleaned_data.get('tag')
        self.validator.validate_tag(tag)
        return tag

    def clean_time_zone(self):
        time_zone = self.cleaned_data.get('time_zone')
        self.validator.validate_time_zone(time_zone)
        return time_zone

    def clean(self):
        self.validator.validate(**self.cleaned_data)
        return super().clean()
