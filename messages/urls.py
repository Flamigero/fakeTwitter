"""Messages urls"""

# Django
from django.urls import path

# Views
from .views import Feed

urlpatterns = [
    path('', Feed.as_view(), name='feed')
]
