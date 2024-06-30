from django.shortcuts import render
from u_educ_site import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserModel, DetailsModel, FamEducationModel


from .serializers import DetailsModelSerializer, FamEducationModelSerializer, SponsorPreferenceSerializer, UserModelSerializer


# Create your views here.

# Creating a class that creates a list Api view
class SponsorPreferenceList(generics.ListCreateAPIView):
    queryset = models.SponsorPreferences.objects.all()
    serializer_class = SponsorPreferenceSerializer

# Creating a class that updates, retrieves, Destroy Api
class SponsorPreferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SponsorPreferences.objects.all()
    serializer_class = SponsorPreferenceSerializer



# Creating user models from flutter app
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data_user:", data) 
            user = UserModel.objects.create(
                fullName=data.get('fullName', ''),
                email=data.get('email', ''),
                phoneNumber=data.get('phoneNumber', ''),
                password=data.get('password', ''),
            )
            return JsonResponse({'message': 'User created successfully', 'userId': user.id}, status=201)
        except Exception as e:
            print("Error: ", e)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def create_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data_details:", data) 

            details = DetailsModel.objects.create(
                userId=data.get('userId', ''),
                surname=data.get('surname', ''),
                otherNames=data.get('otherNames', ''),
                email=data.get('email', ''),
                phoneNumber=data.get('phoneNumber', ''),
                age=data.get('age', ''),
                gender=data.get('gender', ''),
                address=data.get('address', ''),
                profilePicture=data.get('profilePicture', None),
            )
            return JsonResponse({'message': 'Details saved successfully', 'detailsId': details.id}, status=201)
        except Exception as e:
            print("Error: ", e)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def create_fam_education(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Data received_fam_educ:", data)

            fam_education = FamEducationModel.objects.create(
                userId=data.get('userId', ''),
                fatherStatus=data.get('fatherStatus', ''),
                fatherSurname=data.get('fatherSurname', ''),
                fatherGivenName=data.get('fatherGivenName', ''),
                fatherNationalId=data.get('fatherNationalId', ''),
                fatherNationalIdPictureUrl=data.get('fatherNationalIdPictureUrl', ''),
                motherStatus=data.get('motherStatus', ''),
                motherSurname=data.get('motherSurname', ''),
                motherGivenName=data.get('motherGivenName', ''),
                motherNationalId=data.get('motherNationalId', ''),
                motherNationalIdPictureUrl=data.get('motherNationalIdPictureUrl', ''),
                guardianSurname=data.get('guardianSurname', ''),
                guardianGivenName=data.get('guardianGivenName', ''),
                guardianNationalId=data.get('guardianNationalId', ''),
                guardianNationalIdPictureUrl=data.get('guardianNationalIdPictureUrl', ''),
                studentStatus=data.get('studentStatus', ''),
                regNo=data.get('regNo', ''),
                studentNo=data.get('studentNo', ''),
                courseName=data.get('courseName', ''),
                college=data.get('college', ''),
                artsOrSciences=data.get('artsOrSciences', ''),
                yearOfStudy=data.get('yearOfStudy', ''),
                currentCGPA=data.get('currentCGPA', ''),
                tuitionAmountPerSemester=data.get('tuitionAmountPerSemester', ''),
                pictureOfPortalUrl=data.get('pictureOfPortalUrl', ''),
                schoolName=data.get('schoolName', ''),
                schoolLocation=data.get('schoolLocation', ''),
                yearOfSitting=data.get('yearOfSitting', ''),
                subjectOneName=data.get('subjectOneName', ''),
                subjectOneGrade=data.get('subjectOneGrade', ''),
                subjectOnePoints=data.get('subjectOnePoints', ''),
                subjectTwoName=data.get('subjectTwoName', ''),
                subjectTwoGrade=data.get('subjectTwoGrade', ''),
                subjectTwoPoints=data.get('subjectTwoPoints', ''),
                subjectThreeName=data.get('subjectThreeName', ''),
                subjectThreeGrade=data.get('subjectThreeGrade', ''),
                subjectThreePoints=data.get('subjectThreePoints', ''),
                subsidiaryOneName=data.get('subsidiaryOneName', ''),
                subsidiaryOneGrade=data.get('subsidiaryOneGrade', ''),
                subsidiaryOnePoints=data.get('subsidiaryOnePoints', ''),
                subsidiaryTwoName=data.get('subsidiaryTwoName', ''),
                subsidiaryTwoGrade=data.get('subsidiaryTwoGrade', ''),
                subsidiaryTwoPoints=data.get('subsidiaryTwoPoints', ''),
                totalPoints=data.get('totalPoints', ''),
                pictureOfPassSlipUrl=data.get('pictureOfPassSlipUrl', ''),
            )

            return JsonResponse({'message': 'Family education details saved successfully', 'famEducationId': fam_education.id}, status=201)
        except Exception as e:
            print("Error :", e)
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)