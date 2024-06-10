from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.role
    

def calculate_tuition_weight(min_tuition, max_tuition):
    if min_tuition is not None and max_tuition is not None:
        range_tuition = max_tuition - min_tuition
        weight = range_tuition / (max_tuition + min_tuition)
        return weight
    return 0.0

class SponsorPreferences(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    preferred_student_gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('any', 'Any'),
    ], default='any', help_text="Preferred gender of the student.")

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
        validators=[MaxValueValidator(0)], 
        blank=True, 
        null=True,
        help_text="Maximum tuition amount the sponsor is willing to provide."
    )

    preferred_student_courses = models.CharField(max_length=20, choices=[
        ('sciences', 'Sciences'),
        ('arts', 'Arts'),
        ('any', 'Any'),
    ], default='any', help_text="Preferred course of study for the student.")

    weight_student_gender = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight_student_courses = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight_tuition = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
    
    def calculate_weights(self):
        weights = {}

        if self.preferred_student_gender == 'female':
            weights['preferred_student_gender'] = 1.0
        else:
            weights['preferred_student_gender'] = 0.5

        if self.student_courses == 'sciences':
            weights['student_courses'] = 1.0
        else:
            weights['student_courses'] = 0.8
        
        weights['tuition_amount'] = calculate_tuition_weight(self.tuition_amount_min, self.tuition_amount_max)

        self.save()

        
    def average_weight(self):
        weights = [self.weight_gender, self.weight_courses]
        return sum(weights) / len(weights)
