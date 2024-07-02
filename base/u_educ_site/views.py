from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.utils.text import slugify

from apis.models import DetailsModel, FamEducationModel, UserModel 
from django.db.models import Q

from .forms import SignupForm, RoleForm, SponsorPreferencesForm, MappingsForm
from .models import SponsorPreferences, Mappings

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



@login_required
def home(request):
    # Fetch random image URL (replace with your actual logic to fetch random image)
    image_urls = [
        '/static/home/img/bg4.jpg',
        '/static/home/img/bg3.jpg',
        '/static/home/img/bg1.jpg',
        '/static/home/img/bg2.jpg',
    ]
    random_image_url = random.choice(image_urls)

    sponsor_preferences = get_object_or_404(SponsorPreferences, user=request.user)
    users_with_details = UserModel.objects.filter(email__in=DetailsModel.objects.values('email'))

    # Combine data for each user
    combined_data = []
    for user in users_with_details:
        details_instance = DetailsModel.objects.get(email=user.email)
        try:
            education_instance = FamEducationModel.objects.get(userId=details_instance.userId)
        except FamEducationModel.DoesNotExist:
            education_instance = None

        # if sponsor_preferences.preferred_student_gender != 'any' and details_instance.gender != sponsor_preferences.preferred_student_gender:
        #     continue
        # if sponsor_preferences.preferred_student_courses != 'any' and education_instance and education_instance.artsOrSciences != sponsor_preferences.preferred_student_courses:
        #     continue
        # if education_instance and sponsor_preferences.tuition_amount_min is not None and sponsor_preferences.tuition_amount_max is not None:
        #     tuition = float(education_instance.tuitionAmountPerSemester)
        #     if not (sponsor_preferences.tuition_amount_min <= tuition <= sponsor_preferences.tuition_amount_max):
        #         continue

        combined_data.append({
            'user': user,
            'details': details_instance,
            'education': education_instance,
        })

    # Sort the combined data, prioritizing those with guardian information
    combined_data.sort(key=lambda x: (x['education'] is not None and x['education'].guardianSurname))

    context = {
        'random_image_url': random_image_url,
        'page_title': "Sponsor's Dashboard",
        'combined_data': combined_data,
    }

    return render(request, 'dashboard.html', context)



@login_required(login_url='/login')
def addStudent(request, pk):
    sponsor_preferences = get_object_or_404(SponsorPreferences, user=request.user)
    student = get_object_or_404(UserModel, id=pk)
    details_instance = get_object_or_404(DetailsModel, email=student.email)
    
    try:
        education_instance = FamEducationModel.objects.get(userId=details_instance.userId)
    except FamEducationModel.DoesNotExist:
        education_instance = None

    if request.method == 'POST':
        student_full_name = student.fullName
        student_email = student.email
        student_gender = details_instance.gender if details_instance.gender else ''
        year_of_study = education_instance.yearOfStudy if education_instance and education_instance.yearOfStudy else ''
        tuition_amount_per_semester = education_instance.tuitionAmountPerSemester if education_instance and education_instance.tuitionAmountPerSemester else ''

        mapping = Mappings(
            sponsor=request.user,
            studentFullName=student_full_name,
            studentEmail=student_email,
            studentGender=student_gender,
            yearOfStudy=year_of_study,
            tuitionAmountPerSemester=tuition_amount_per_semester,
            status='Pending'
        )
        mapping.save()

        messages.success(request, 'Student has been added successfully.')
        return redirect('home')

    context = {
        'student': student,
        'details': details_instance,
        'sponsor_preferences' : sponsor_preferences,
        'education': education_instance,
        'student_matches': True,
        'page_title': 'Add Student',
    }

    return render(request, 'add_student.html', context)


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
    active_mappings = Mappings.objects.filter(sponsor=request.user, status='Accepted')
    context = {
        'active_mappings': active_mappings,
        'page_title': "Active Sponsor's Mappings",
    }
    return render(request, "mappings.html", context)

@login_required(login_url='/login')
def mapRequests(request):
    mappings = Mappings.objects.filter(sponsor=request.user)
    context = {
        'page_title': 'Mapping Pending Requests',
        'mappings' : mappings    
    }
    return render(request, "map_requests.html", context)

@login_required(login_url='/login')
def deleteMapRequest(request, pk):
    # mapping = Mappings.objects.get(id=pk)
    mapping = get_object_or_404(Mappings, id=pk)
    if request.method == 'POST':
        mapping.delete()
        messages.success(request, 'Pending Mapping Request Has Been Deleted')
        return redirect('map_requests')
    
    context = {
        'mapping' : mapping,
        'page_title': 'Delete Pending Mapping Request',
    }

    return render(request, 'delete_map_request.html', context)

@login_required(login_url='/login')
def endMapping(request, pk):
    # mapping = Mappings.objects.get(id=pk)
    mapping = get_object_or_404(Mappings, id=pk)
    if request.method == 'POST':
        mapping.delete()
        messages.success(request, 'Active Mapping Request Has Been Ended')
        return redirect('mappings')
    
    context = {
        'mapping' : mapping,
        'page_title': 'Endingg Mapping With Student',
    }

    return render(request, 'end_mapping.html', context)