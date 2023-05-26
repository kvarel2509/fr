from django.db import models

from .models import Client
from .validators import ClientValidator


class ClientRepository(models.Manager):
    def __init__(self, validator=ClientValidator()):
        self.validator = validator

    def all_clients(self):
        return Client.objects.all()

    def filter_clients(self, **kwargs):
        return Client.objects.filter(**kwargs)

    def create_client(self, phone, mobile_operator_code, tag, time_zone):
        self.validator.validate_phone(phone)
        self.validator.validate_mobile_operator_code(mobile_operator_code)
        self.validator.validate_tag(tag)
        self.validator.validate_time_zone(time_zone)
        self.validator.validate(phone=phone, mobile_operator_code=mobile_operator_code, tag=tag, time_zone=time_zone)
        client = Client(phone=phone, mobile_operator_code=mobile_operator_code, tag=tag, time_zone=time_zone)
        client.save()
        return client
