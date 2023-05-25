from django.contrib import admin

from clients.forms import ClientAdminForm
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ('id', 'phone', 'mobile_operator_code', 'tag', 'time_zone')
