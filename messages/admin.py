"""Messages admin"""

# Django
from django.contrib import admin

# Models
from .models import Message

@admin.register(Message)
class MessageProfile(admin.ModelAdmin):
    """Message admin"""

    list_display = ('pk','user', 'text')

    readonly_fields = ('created_at', 'updated_at')