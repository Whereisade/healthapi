from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_id', 'patient', 'doctor', 'date', 'time', 'status', 'reason']
        read_only_fields= ['status', 'patient'] 