from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignupForm, RoleForm

# Create your views here.

def signup(request):
    form = SignupForm()
    context = {
        'username' : '',
        'email' : '',
        'password1' : '',
        'password2' : '',
        'form' : form
    }
    if request.method == 'POST':
        form = SignupForm(request.POST)
        context['username'] = request.POST.get('username')
        context['email'] = request.POST.get('email')
        context['password1'] = request.POST.get('password1')
        context['password2'] = request.POST.get('password2')
        context['form'] = form

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            new_user = authenticate(username=username, password=password)
            
            role = RoleForm({'user': new_user.id, 'role': 'Sponsor'})
            role.save()

            if new_user is not None:
                login(request, new_user)
                return redirect("home")
        else:
            messages.error(request, form.errors)

    return render(request, "auth/signup.html", context)

def loginUser(request):
    context = {
        'username' : '',
        'password' : ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        context['username'] = username
        context['password'] = password
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Invalid credentials")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "No user with these details available")

    return render(request, "auth/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def home(request):
    return render(request, "dashboard.html")

@login_required(login_url='/login')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url='/login')
def mappings(request):
    return render(request, "mapping.html")

@login_required(login_url='/login')
def donations(request):
    return render(request, "donations.html")