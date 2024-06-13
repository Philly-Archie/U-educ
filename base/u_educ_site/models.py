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

    # profileImage = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'