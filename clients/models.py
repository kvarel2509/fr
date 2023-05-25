from django.db import models


class Client(models.Model):
    phone = models.CharField(max_length=255)
    mobile_operator_code = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=255)

    class Meta:
        db_table = 'client'
        indexes = [
            models.Index(fields=['mobile_operator_code', 'tag']),
            models.Index(fields=['mobile_operator_code']),
            models.Index(fields=['tag'])
        ]
