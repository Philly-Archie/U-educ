from django.shortcuts import render
from u_educ_site import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import SponsorPreferenceSerializer

# Create your views here.

# Creating a class that creates a list Api view
class SponsorPreferenceList(generics.ListCreateAPIView):
    queryset = models.SponsorPreferences.objects.all()
    serializer_class = SponsorPreferenceSerializer

# Creating a class that updates, retrieves, Destroy Api
class SponsorPreferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SponsorPreferences.objects.all()
    serializer_class = SponsorPreferenceSerializer




