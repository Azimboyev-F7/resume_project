from django.contrib import admin

from .models import Recieve
# Register your models here.


class RecieveAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']



admin.site.register(Recieve, RecieveAdmin)
