

from rest_framework import serializers
from .models import Appointment
from doctors.serializers import DoctorProfileSerializer, DoctorProfile
from users.serializers import PatientDetailsSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    
    patient = PatientDetailsSerializer(read_only=True)
    # patient = serializers.StringRelatedField()
    
    
    doctor = DoctorProfileSerializer(read_only=True)
    
    
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorProfile.objects.all(), 
        source='doctor', 
        write_only=True
    )

    class Meta:
        model = Appointment
        
        fields = ['appointment_id', 'patient', 'doctor', 'doctor_id', 'date', 'time', 'status', 'reason']
        read_only_fields = ['patient']
