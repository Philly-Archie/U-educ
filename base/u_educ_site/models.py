from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now
import os
from math import ceil


# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.role
    
class SponsorPreferences(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zipCode = models.CharField(max_length=20, blank=True, null=True)

    preferred_student_gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('any', 'Any'),
    ], default='any', help_text="Preferred gender of the student.")

    preferred_student_courses = models.CharField(max_length=20, choices=[
        ('sciences', 'Sciences'),
        ('arts', 'Arts'),
        ('any', 'Any'),
    ], default='any', help_text="Preferred course of study for the student.")

    tuition_amount_min = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        blank=True, 
        null=True,
        help_text="Minimum tuition amount the sponsor is willing to provide."
    )
    tuition_amount_max = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        blank=True, 
        null=True,
        help_text="Maximum tuition amount the sponsor is willing to provide."
    )


    weight_student_gender = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight_student_courses = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight_tuition = models.FloatField(default=0.0)

    profileImage = models.ImageField(upload_to = 'profile_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName} ({self.email})'
    
    def calculate_tuition_weight(self):
        if self.tuition_amount_min is not None and self.tuition_amount_max is not None:
            range_tuition = self.tuition_amount_max - self.tuition_amount_min
            weight = range_tuition / (self.tuition_amount_max + self.tuition_amount_min)
            return weight
        return 0.0   

    def calculate_weights(self):
        if self.preferred_student_gender == 'female':
            self.weight_student_gender = 1.0
        else:
            self.weight_student_gender = 0.5

        if self.preferred_student_courses == 'sciences':
            self.weight_student_courses = 1.0
        else:
            self.weight_student_courses = 0.8
        
        self.weight_tuition = self.calculate_tuition_weight()

        self.save()

    def average_weight(self):
        weights = [self.weight_student_gender, self.weight_student_courses, self.weight_tuition]
        my_average_weight = sum(weights) / len(weights)
        rounded_average_weight = round(my_average_weight, 3)
        return (abs(rounded_average_weight))
    
class Mappings(models.Model):
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE)
    studentFullName = models.CharField(max_length=500)
    studentEmail = models.EmailField()
    studentPhoneNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.sponsor} {self.studentFullName} {self.studentEmail}'