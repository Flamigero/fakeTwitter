"""Messages form"""

# Django
from django import forms

# Models
from messages.models import Message

class TweetForm(forms.ModelForm):
    """Tweet form"""

    class Meta:
        """Form settings"""
        
        model = Message
        fields = ('user', 'text')