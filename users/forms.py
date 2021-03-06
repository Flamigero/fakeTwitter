"""Users forms"""

# Django
from django import forms

# Models
from users.models import User, Profile

class SignUpForm(forms.Form):
    """Sign Up Form"""

    username = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput())
    phone = forms.IntegerField()

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=70, widget=forms.PasswordInput())

    def clean_email(self):
        """Email must be unique"""
        email = self.cleaned_data['email']
        email_exist = User.objects.filter(email=email).exists()

        if(email_exist):
            raise forms.ValidationError("Email must be unique")

        return email

    def clean(self):
        """Verify passwords match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['rePassword']

        if password != password_confirmation:
            raise forms.ValidationError("Passwords don't match")

        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            phone_number=data['phone'],
            password=data['password']
        )
        profile = Profile.objects.create(user=user)
        profile.save()

class UpdateProfileForm(forms.Form):
    """Update profile form"""

    id = forms.IntegerField()
    picture = forms.ImageField(required=False)
    fname = forms.CharField()
    lname = forms.CharField()
    description = forms.CharField()
    phone = forms.IntegerField()

    def save(self):
        """Update user and profile"""
        data = self.cleaned_data

        user = User.objects.filter(pk=data['id'])[0]
        profile =  Profile.objects.filter(user=user)[0]

        user.first_name = data['fname']
        user.last_name = data['lname']
        user.phone_number = data['phone']
        profile.description = data['description']
        if data['picture']:
            profile.picture = data['picture']

        user.save()
        profile.save()
