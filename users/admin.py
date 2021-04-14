"""
Users models admin
"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """User admin"""

    list_display = ('email', 'username', 'phone_number', 'is_staff')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display = ('user', 'is_authenticated', 'picture')

    readonly_fields = ('created_at', 'updated_at')