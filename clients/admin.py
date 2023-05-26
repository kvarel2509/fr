from django.contrib import admin

from .forms import ClientAdminForm
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ('id', 'phone', 'mobile_operator_code', 'tag', 'time_zone')
