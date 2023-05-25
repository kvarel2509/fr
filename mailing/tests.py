from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .logic.perform_mailing.model import is_time_of_client_in_valid_mailing_time_interval
from .validators import MailingValidator, FilterValidator, is_start_date_expired, validate_start_date_expired


class TestFilterValidator(TestCase):
    def setUp(self) -> None:
        self.filter_validator = FilterValidator(['key1', 'key2'])

    def test_valid_filters(self):
        datasets = [{'key1': 1, 'key2': 2}, {'key1': 'a'}, {'key2': 'v'}, {}]
        for dataset in datasets:
            self.assertIsNone(self.filter_validator(dataset))

    def test_invalid_filters(self):
        datasets = [['key1'], {'key3': 1}, {'key1': 1, 'key3': 2}, {'key1': {'key1': 'a'}}]
        for dataset in datasets:
            with self.assertRaises(ValidationError):
                self.filter_validator(dataset)


class TestMailingValidator(TestCase):
    def setUp(self) -> None:
        self.validator = MailingValidator()

    def test_valid_filters(self):
        datasets = [{'mobile_operator_code': 1, 'tag': 2}, {'mobile_operator_code': 'a'}, {'tag': 'v'}, {}]
        for dataset in datasets:
            self.assertIsNone(self.validator.validate_filters(dataset))

    def test_invalid_filters(self):
        datasets = [['tag'], {'key3': 1}, {'tag': 1, 'key3': 2}, {'tag': {'tag': 'a'}}]
        for dataset in datasets:
            with self.assertRaises(ValidationError):
                self.validator.validate_filters(dataset)

    def test_valid_kwargs_in_validate_method(self):
        datasets = [
            {'start_date': timezone.now(), 'end_date': timezone.now() + timezone.timedelta(days=1)},
            {'start_date': timezone.now()}
        ]
        for dataset in datasets:
            self.assertIsNone(self.validator.validate(**dataset))

    def test_invalid_kwargs_in_validate_method(self):
        datasets = [
            {'start_date': timezone.now(), 'end_date': timezone.now() - timezone.timedelta(days=1)},
        ]
        for dataset in datasets:
            with self.assertRaises(ValidationError):
                self.validator.validate(**dataset)


class TestStartDateExpired(TestCase):
    def setUp(self) -> None:
        self.gt_date = timezone.now() + timezone.timedelta(days=1)
        self.lt_date = timezone.now() - timezone.timedelta(days=1)

    def test_is_start_date_expired(self):
        self.assertFalse(is_start_date_expired(self.gt_date))
        self.assertTrue(is_start_date_expired(self.lt_date))

    def test_validate_start_date_expired(self):
        self.assertIsNone(validate_start_date_expired(self.gt_date))
        with self.assertRaises(ValidationError):
            validate_start_date_expired(self.lt_date)


class TestIsTimeOfClientInValidMailingTimeInterval(TestCase):
    def setUp(self) -> None:
        self.curr_time = timezone.now()

    def test_time_interval_start_lt_time_interval_end(self):
        start_time = (self.curr_time - timezone.timedelta(hours=3)).time()
        end_time = (self.curr_time + timezone.timedelta(hours=3)).time()
        for tz in ['Etc/GMT+6', 'Etc/GMT-6']:
            self.assertFalse(is_time_of_client_in_valid_mailing_time_interval(start_time, end_time, tz))
        for tz in ['Etc/GMT+2', 'Etc/GMT-2', 'Etc/GMT']:
            self.assertTrue(is_time_of_client_in_valid_mailing_time_interval(start_time, end_time, tz))

    def test_time_interval_start_gt_time_interval_end(self):
        start_time = (self.curr_time + timezone.timedelta(hours=3)).time()
        end_time = (self.curr_time - timezone.timedelta(hours=3)).time()
        for tz in ['Etc/GMT+6', 'Etc/GMT-6']:
            self.assertTrue(is_time_of_client_in_valid_mailing_time_interval(start_time, end_time, tz))
        for tz in ['Etc/GMT+2', 'Etc/GMT-2', 'Etc/GMT']:
            self.assertFalse(is_time_of_client_in_valid_mailing_time_interval(start_time, end_time, tz))
