from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from dataclasses import field
from django.forms import ModelForm

from .models import Role, SponsorPreferences, Mappings


# Adding form data from here
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class SponsorPreferencesForm(ModelForm):
    class Meta:
        model = SponsorPreferences
        fields = [
            'firstName', 'lastName', 'email', 'phoneNumber', 'address',
            'city', 'state', 'country', 'zipCode', 'preferred_student_gender',
            'preferred_student_courses', 'tuition_amount_min', 'tuition_amount_max', 'profileImage'
        ]

class MappingsForm(ModelForm):
    class Meta:
        model = Mappings
        fields = '__all__'
