from django.forms import DateTimeInput, TimeInput


class DateTimeWidget(DateTimeInput):
    input_type = 'datetime-local'


class TimeWidget(TimeInput):
    input_type = 'time'
