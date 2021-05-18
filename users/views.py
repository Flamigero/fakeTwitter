"""
Users views
"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView

# Forms
from users.forms import SignUpForm, UpdateProfileForm

# Models
from users.models import Profile, User
from messages.models import Message

class Login(View):
    template_name = 'users/login.html'
    email = ''
    password = ''

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        self.email = request.POST['email']
        self.password = request.POST['password']

        user = authenticate(request, email=self.email, password=self.password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, self.template_name, {
                'error': 'Invalid user or password'
            })

class Signup(FormView):
    template_name = 'users/signUp.html'
    form_class = SignUpForm
    success_url = '/users/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Logout(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class ProfileV(ListView):
    template_name = 'users/profile.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        self.userProfile = User.objects.filter(pk=self.kwargs['id'])[0]
        return Message.objects.filter(user=self.userProfile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userProfile'] = self.userProfile
        return context

class EditProfile(FormView):
    template_name = 'users/editprofile.html'
    form_class = UpdateProfileForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.userId = kwargs['id']

        if request.user.pk != kwargs['id']:
            return redirect('feed')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userProfile = User.objects.filter(pk=self.userId)[0]
        profile = Profile.objects.filter(user=userProfile)[0]

        context['userProfile'] = userProfile
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)