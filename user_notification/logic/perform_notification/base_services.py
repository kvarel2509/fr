from abc import ABC, abstractmethod


class NotificationPerformer(ABC):
    def run_notification(self, subscription_name, *args, **kwargs):
        contacts = self.get_contacts(subscription_name)
        data = self.get_data()
        text = self.format(data)

        for contact in contacts:
            self.notify(contact, text)

    @abstractmethod
    def get_contacts(self, subscription_name): ...

    @abstractmethod
    def notify(self, contact, information): ...

    @abstractmethod
    def get_data(self): ...

    def format(self, data):
        return data
