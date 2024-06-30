from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.utils.text import slugify

from apis.models import DetailsModel, FamEducationModel, UserModel 
from django.db.models import Q

from .forms import SignupForm, RoleForm, SponsorPreferencesForm
from .models import SponsorPreferences

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
                return redirect("sponsor_preferences")
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


def home(request):
    # Fetch random image URL (replace with your actual logic to fetch random image)
    image_urls = [
        '/static/home/img/bg4.jpg',
        '/static/home/img/bg3.jpg',
        '/static/home/img/bg1.jpg',
        '/static/home/img/bg2.jpg',
    ]
    random_image_url = random.choice(image_urls)

    # Retrieve users from UserModel where email matches with DetailsModel
    users_with_details = UserModel.objects.filter(email__in=DetailsModel.objects.values('email'))

    # Combine data for each user
    combined_data = []
    for user in users_with_details:
        # Retrieve DetailsModel instance based on email
        details_instance = DetailsModel.objects.get(email=user.email)

        # Retrieve FamEducationModel instance associated with DetailsModel
        education_instance = FamEducationModel.objects.get(userId=details_instance)

        # Prepare combined data for the template
        combined_data.append({
            'user': user,
            'details': details_instance,
            'education': education_instance,
        })

    context = {
        'random_image_url': random_image_url,
        'combined_data': combined_data,
    }

    return render(request, 'student_information.html', context)





# @login_required(login_url='/login')
# def home(request):
#     image_urls = [
#         '/static/home/img/bg4.jpg',
#         '/static/home/img/bg3.jpg',
#         '/static/home/img/bg1.jpg',
#         '/static/home/img/bg2.jpg',
#     ]
    
#     random_image_url = random.choice(image_urls)
#     users = UserModel.objects.exclude(fullName__isnull=True).exclude(fullName='')
#     user_details = DetailsModel.objects.all()
#     user_educations = FamEducationModel.objects.all()

#     combined_data = []

#     for user in users:
#         details = user_details.filter(userId=user.id).first()
#         if not details:
#             details = user_details.filter(email=user.email).first()
#             if not details:
#                 details = user_details.filter(surname=user.fullName.split()[0]).first()

#         education = user_educations.filter(userId=user.id).first()
        
#         combined_data.append({
#             'user': user,
#             'details': details,
#             'education': education,
#         })
    
#     context = {
#         'random_image_url': random_image_url,
#         'page_title': 'U-EDUC Sponsor Dashboard',
#         'combined_data': combined_data,
#     }
#     return render(request, "dashboard.html", context)


@login_required(login_url='/login')
def sponsorPreferences(request):
    if request.method == 'POST':
        form = SponsorPreferencesForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            sponsor_preferences = form.save(commit=False)
            sponsor_preferences.user = request.user
            sponsor_preferences.calculate_weights()

            sponsor_preferences.save()
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Error submitting the form")
    else:
        form = SponsorPreferencesForm()
    
    context = {
        'form': form,
        'inactive_sidebar': True,
    }

    return render(request, "sponsor_preferences.html", context)



@login_required(login_url='/login')
def profile(request):
    my_image_urls = [
        '/static/home/img/bg4.jpg',
        '/static/home/img/bg3.jpg',
        '/static/home/img/bg1.jpg',
        '/static/home/img/bg2.jpg',
    ]
    my_random_image_url = random.choice(my_image_urls)

    sponsor_preference = get_object_or_404(SponsorPreferences, user=request.user)
    
    context = {
        'my_random_image_url': my_random_image_url,
        'page_title': "Sponsor's Profile",
        'sponsor_preference' : sponsor_preference,
    }
    return render(request, "profile.html", context)

def editProfile(request):
    sponsor_preference = get_object_or_404(SponsorPreferences, user=request.user)

    if request.method == 'POST':
        form = SponsorPreferencesForm(request.POST, request.FILES, instance=sponsor_preference)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
            messages.error(request, "Error submitting the form")
        


@login_required(login_url='/login')
def mappings(request):
    context ={
        'page_title': "Active Sponsor's Mappings",
    }
    return render(request, "mappings.html", context)

@login_required(login_url='/login')
def mapRequests(request):
    context = {
        'page_title': 'Mapping Pending Requests'
    }
    return render(request, "map_requests.html", context)