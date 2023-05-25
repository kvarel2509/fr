from django.db import models

from users.models import User


class Subscription(models.Model):
    name = models.SlugField(primary_key=True)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(User, through='UserSubscription')

    class Meta:
        db_table = 'subscription'


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_subscription'
