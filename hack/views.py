from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

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
            return render(request, 'success.html')  # Replace 'home' with your desired URL name
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
                return render(request, 'index.html')
            else:
                # User does not exist, provide a sign-up option
                return render(request, 'signup.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
