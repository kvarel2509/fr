from django import template

from mailing.validators import is_start_date_expired

register = template.Library()


@register.filter
def date_has_expired(date):
    return is_start_date_expired(date)
