"""Messages urls"""

# Django
from django.urls import path

# Views
from .views import feed

urlpatterns = [
    path('', feed, name='feed')
]
