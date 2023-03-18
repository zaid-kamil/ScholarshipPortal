from django import forms
from django.contrib.auth.models import User

from .models import Profile

INVALID_USERNAMES = ['admin', 'administrator', 'root',
                     'sudo', 'superuser', 'super', 'user', 'staff', 'moderator', 'admin1']


# login form
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return email


# register form
class RegisterForm(forms.Form):
    username = forms.CharField(help_text='Enter a valid username')
    email = forms.EmailField(help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password',
                                help_text='password must be at least 6 characters long')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password",
                                help_text='must match the password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'gender', 'phone', 'address', 'city', 'state', 'country']
