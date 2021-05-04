"""
Users URLs
"""

# Django
from django.urls import path

# Views
from .views import login_view, signup_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signUp/', signup_view, name="signUp"),
    path('logout/', logout_view, name="logout")
]
