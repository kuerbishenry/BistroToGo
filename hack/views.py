from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from Forms import *

from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return render(request, 'orderScreen.html')  # Replace 'home' with your desired URL name
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # Redirect to a success page or the home page
                return render(request, 'orderScreen.html')
            else:
                # User does not exist, provide a sign-up option
                return render(request, 'signup.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_update(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('some_view_name')  # redirect to a success page or something similar
    else:
        form = UserProfileForm(instance=instance)

    return render(request, 'path_to_template.html', {'form': form})
