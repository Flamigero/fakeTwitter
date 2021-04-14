"""
Users model
"""

# Django
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    """User model"""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }
    )

    phone_regex = RegexValidator(
       regex=r'\+?1?\d{9,15}$',
       message='Phone number must be entered in the right format'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.username

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField('user description', max_length=255)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    is_authenticated = models.BooleanField('user is autheticated', default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
