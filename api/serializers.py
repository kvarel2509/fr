from rest_framework import serializers

from clients.models import Client
from clients.validators import ClientValidator
from mailing.models import Mailing
from mailing.validators import MailingValidator, validate_start_date_expired


class ClientSerializer(serializers.ModelSerializer):
    validator = ClientValidator()

    class Meta:
        model = Client
        fields = ('id', 'phone', 'mobile_operator_code', 'tag', 'time_zone')

    def validate_phone(self, value):
        self.validator.validate_phone(value)
        return value

    def validate_mobile_operator_code(self, value):
        self.validator.validate_mobile_operator_code(value)
        return value

    def validate_tag(self, value):
        self.validator.validate_tag(value)
        return value

    def validate_time_zone(self, value):
        self.validator.validate_time_zone(value)
        return value

    def validate(self, attrs):
        self.validator.validate(**attrs)
        return attrs


class MailingSerializer(serializers.ModelSerializer):
    filters = serializers.JSONField(required=False, initial=dict)
    validator = MailingValidator()

    class Meta:
        model = Mailing
        fields = ('id', 'start_date', 'message', 'filters', 'end_date', 'time_interval_start', 'time_interval_end')

    def validate_start_date(self, value):
        self.validator.validate_start_date(value)
        return value

    def validate_message(self, value):
        self.validator.validate_message(value)
        return value

    def validate_filters(self, value):
        self.validator.validate_filters(value)
        return value

    def validate_end_date(self, value):
        self.validator.validate_end_date(value)
        return value

    def validate_time_interval_start(self, value):
        self.validator.validate_time_interval_start(value)
        return value

    def validate_time_interval_end(self, value):
        self.validator.validate_time_interval_end(value)
        return value

    def validate(self, attrs):
        if self.instance and self.instance.start_date:
            validate_start_date_expired(self.instance.start_date)
        self.validator.validate(**attrs)
        return attrs
