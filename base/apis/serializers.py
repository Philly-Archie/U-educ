from rest_framework import serializers
from u_educ_site import models


class SponsorPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'firstName',
            'lastName',
            'profileImage',
        )
        model = models.SponsorPreferences