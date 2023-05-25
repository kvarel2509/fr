from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Client
from .validators import ClientValidator


class TestClientValidator(TestCase):
    def setUp(self) -> None:
        self.validator = ClientValidator()

    def test_valid_phone(self):
        phones = ['79001001010', 79001001010]
        for phone in phones:
            self.assertIsNone(self.validator.validate_phone(phone))

    def test_invalid_phone(self):
        phones = ['89001001010', '7900100101', '790010010101', '7invalid']
        for phone in phones:
            with self.assertRaises(ValidationError):
                self.validator.validate_phone(phone)

    def test_valid_time_zone(self):
        time_zones = ['Europe/Moscow', 'Africa/Banjul', 'America/Phoenix', 'WET', 'UTC']
        for time_zone in time_zones:
            self.assertIsNone(self.validator.validate_time_zone(time_zone))

    def test_invalid_time_zone(self):
        time_zones = ['America/Port-au', 'Russia/Paris']
        for time_zone in time_zones:
            with self.assertRaises(ValidationError):
                self.validator.validate_time_zone(time_zone)


class TestClientManager(TestCase):
    def setUp(self) -> None:
        self.c1 = Client.objects.create_client(
            phone='79001001010', mobile_operator_code='mts', tag='tag1', time_zone='Europe/Moscow'
        )
        self.c2 = Client.objects.create_client(
            phone='79001001011', mobile_operator_code='beeline', tag='tag2', time_zone='Europe/Moscow'
        )
        self.c3 = Client.objects.create_client(
            phone='79001001012', mobile_operator_code='mts', time_zone='Europe/Moscow'
        )

    def test_filters_with_mobile_operator_code(self):
        clients = Client.objects.filter_clients(mobile_operator_code='mts')
        self.assertIn(self.c1, clients)
        self.assertIn(self.c3, clients)
        self.assertNotIn(self.c2, clients)

    def test_filters_with_tag(self):
        clients = Client.objects.filter_clients(tag='tag1')
        self.assertIn(self.c1, clients)
        self.assertNotIn(self.c3, clients)
        self.assertNotIn(self.c2, clients)

    def test_filters_with_tag_and_mobile_operator_code(self):
        clients = Client.objects.filter_clients(mobile_operator_code='beeline', tag='tag2')
        self.assertIn(self.c2, clients)
        self.assertNotIn(self.c1, clients)
        self.assertNotIn(self.c3, clients)
