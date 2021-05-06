"""
Users views
"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Forms
from users.forms import SignUpForm

# Models
from users.models import User
from messages.models import Message

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

def profile_view(request, id):
    """Profile view"""
    userProfile = User.objects.filter(pk=id)
    tweets = Message.objects.filter(user=userProfile[0])

    return render(request, 'users/profile.html', {
        'userProfile': userProfile[0],
        'tweets': tweets
    })