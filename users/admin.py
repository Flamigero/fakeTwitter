"""
Users models admin
"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """User model admin"""

    list_display = ('email', 'username', 'phone_number', 'is_staff')