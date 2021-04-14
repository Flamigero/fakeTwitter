"""Messages model"""

# Django
from django.db import models

# Models
from users.models import User

class Message(models.Model):
    """Message model"""

    text = models.TextField('message text', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    retweet = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
    