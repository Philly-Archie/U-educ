from django.shortcuts import render, redirect

# Create your views here.

def signup(request):
    return render(request, "auth/signup.html")

def login(request):
    return render(request, "auth/login.html")

def logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, "dashboard.html")