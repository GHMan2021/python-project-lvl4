from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'first_name',
        'last_name',
        'username',
        'is_staff',
    )
    list_display_links = (
        'first_name',
        'last_name'
    )


admin.site.register(CustomUser, CustomUserAdmin)
