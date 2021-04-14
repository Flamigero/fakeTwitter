"""
Users views
"""

# Django
from django.shortcuts import render, redirect

def login_view(request):
    """Login view"""

    return render(request, 'users/login.html')