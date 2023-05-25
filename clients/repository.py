from django.db import models

from clients.models import Client
from clients.validators import ClientValidator


class ClientRepository(models.Manager):
    def __init__(self, validator=ClientValidator(), model=Client):
        self.model = model
        self.validator = validator

    def all_clients(self):
        return self.model.objects.all()

    def filter_clients(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def create_client(self, phone, mobile_operator_code, tag, time_zone):
        self.validator.validate_phone(phone)
        self.validator.validate_mobile_operator_code(mobile_operator_code)
        self.validator.validate_tag(tag)
        self.validator.validate_time_zone(time_zone)
        self.validator.validate(phone=phone, mobile_operator_code=mobile_operator_code, tag=tag, time_zone=time_zone)
        client = self.model(phone=phone, mobile_operator_code=mobile_operator_code, tag=tag, time_zone=time_zone)
        client.save()
        return client
