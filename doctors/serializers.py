from rest_framework import serializers
from .models import DoctorProfile

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['id', 'name', 'specialty', 'bio', 'availability']
