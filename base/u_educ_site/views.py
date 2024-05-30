from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def signup(request):
    return render(request, "auth/signup.html")

def login(request):
    return render(request, "auth/login.html")

def logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def home(request):
    return render(request, "dashboard.html")