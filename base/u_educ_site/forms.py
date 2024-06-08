from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from dataclasses import field
from django.forms import ModelForm

from .models import Role


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
