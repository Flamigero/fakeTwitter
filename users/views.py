"""
Users views
"""

# Django
from django.shortcuts import render, redirect

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

    return render(request, 'users/login.html')