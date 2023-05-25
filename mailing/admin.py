from django.contrib import admin

from .forms import MailingForm
from .models import Mailing, Message
from .validators import is_start_date_expired


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    form = MailingForm
    list_display = ('id', 'start_date', 'message', 'filters', 'end_date', 'time_interval_start', 'time_interval_end')

    def has_change_permission(self, request, obj=None):
        if obj and obj.start_date and is_start_date_expired(obj.start_date):
            return False
        return super().has_change_permission(request, obj)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'status', 'mailing', 'client')
