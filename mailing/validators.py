from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils import timezone


class MailingValidator:
    @classmethod
    def validate_start_date(cls, value):
        pass

    @classmethod
    def validate_message(cls, value):
        pass

    @classmethod
    def validate_filters(cls, value):
        FilterValidator(['mobile_operator_code', 'tag'])(value)

    @classmethod
    def validate_end_date(cls, value):
        pass

    @classmethod
    def validate_time_interval_start(cls, value):
        pass

    @classmethod
    def validate_time_interval_end(cls, value):
        pass

    @classmethod
    def validate(cls, **kwargs):
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        if end_date and start_date > end_date:
            raise ValidationError('start_date must be earlier than end_date')


@deconstructible
class FilterValidator:
    def __init__(self, allowed_keys):
        self.allowed_keys = allowed_keys

    def __call__(self, value):
        if type(value) is not dict:
            raise ValidationError("Value must be a dictionary")
        for key in value.keys():
            if key not in self.allowed_keys:
                raise ValidationError(f"Key {key} is invalid")
            if type(value[key]) in [list, dict]:
                raise ValidationError(f"Value in key {key} is invalid")

    def __eq__(self, other):
        return all([
            isinstance(other, FilterValidator),
            self.allowed_keys == other.allowed_keys,
        ])


def is_start_date_expired(date):
    return date < timezone.now()


def validate_start_date_expired(date):
    if is_start_date_expired(date):
        raise ValidationError('start_date expired')
