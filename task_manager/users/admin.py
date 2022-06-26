from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    model = CustomUser
    list_display = [
        'first_name',
        'last_name',
        'username',
        'is_staff',
    ]

admin.site.register(CustomUser, CustomUserAdmin)
