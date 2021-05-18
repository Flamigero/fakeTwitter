"""
Users URLs
"""

# Django
from django.urls import path

# Views
from .views import Login, Signup, Logout, ProfileV, EditProfile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signUp/', Signup.as_view(), name='signUp'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:id>', ProfileV.as_view(), name='profile'),
    path('profile/<int:id>/edit', EditProfile.as_view(), name='editProfile')
]
