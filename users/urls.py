"""
Users URLs
"""

# Django
from django.urls import path

# Views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login')
]
