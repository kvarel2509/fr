from user_notification.models import Subscription


class NotificationRepository:
    def get_subscribed_users(self, subscription):
        return subscription.users.all()

    def get_subscription_by_name(self, name):
        return Subscription.objects.get(name=name)
