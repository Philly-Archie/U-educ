from rest_framework import serializers
from u_educ_site import models

from .models import UserModel, FamEducationModel, DetailsModel


class SponsorPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'firstName',
            'lastName',
            'profileImage',
            'address',
            'phoneNumber',
        )
        model = models.SponsorPreferences

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class DetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsModel
        fields = '__all__'

class FamEducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamEducationModel
        fields = '__all__'