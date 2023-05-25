import pytz
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ClientValidator:
    @classmethod
    def validate_phone(cls, value):
        RegexValidator(r'\b7\d{10}\b')(value)

    @classmethod
    def validate_mobile_operator_code(cls, value):
        pass

    @classmethod
    def validate_tag(cls, value):
        pass

    @classmethod
    def validate_time_zone(cls, value):
        if value not in pytz.all_timezones:
            raise ValidationError("Time zone is invalid")

    @classmethod
    def validate(cls, **values):
        pass
