from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']



admin.site.register(User, UserAdmin)
