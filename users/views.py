"""
Users views
"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Forms
from users.forms import SignUpForm

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid user or password'
            })

    return render(request, 'users/login.html')

def signup_view(request):
    """SignUp view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'users/signUp.html', {
        'form': form
    })

def logout_view(request):
    """Log out user"""
    logout(request)
    return redirect('login')