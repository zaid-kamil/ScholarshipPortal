# load default project title from settings.py
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm, ProfileForm
from .models import Profile

title = settings.PROJECT_TITLE

User = get_user_model()  # get the user model


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        pwd = form.cleaned_data.get('password')
        query = User.objects.filter(email__iexact=email).first()
        user = authenticate(request, username=query.username, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('/')
        else:
            messages.error(request, 'Wrong Credentials')
    ctx = {'form': form, 'title': f'{title} | Login'}
    return render(request, "accounts/login.html", ctx)


# register view
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('/')  # redirect to home page
        else:
            messages.error(request, 'Passwords do not match!')
    ctx = {'form': form, 'title': f'{title} | Register'}
    return render(request, "accounts/register.html", ctx)


def logout_view(request):
    # logout the user
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('/')


def profile_view(request):
    # if the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('login')
    ctx = {'title': f'{title} | Profile'}
    #  if the user has not set a profile, redirect to profile setup page else display profile
    profile = Profile.objects.filter(user=request.user)
    if profile.exists():
        ctx['profile'] = profile.first()
        return render(request, 'accounts/profile.html', ctx)
    else:
        messages.error(request, 'You must set up your profile')
        return redirect('profile_setup')


def profile_create(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('accounts:login')
    form = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your Profile Created')
            return redirect('profile')
        except Exception as e:
            messages.error(request, f'Error: {e}')
    ctx = {'form': form, 'title': f'{title} | Profile Setup'}
    return render(request, 'accounts/profile_create.html', ctx)


def profile_update(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('login')
    profile = Profile.objects.filter(user=request.user).first()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Profile Updated')
        return redirect('profile')
    ctx = {'form': form, 'title': f'{title} | Profile Update'}
    return render(request, 'accounts/profile_update.html', ctx)
