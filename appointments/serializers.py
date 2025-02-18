# from rest_framework import serializers
# from .models import Appointment
# from users.models import CustomUser
# from doctors.serializers import DoctorProfileSerializer
# from users.serializers import CustomTokenObtainPairSerializer, RegisterSerializer
# from patient.serializers import PatientProfileSerializer


# class AppointmentSerializer(serializers.ModelSerializer):
#     # patient = serializers.StringRelatedField()
#     # patient = PatientProfileSerializer(read_only=True) 
#     doctor= DoctorProfileSerializer(read_only=True) 

#     class Meta:
#         model = Appointment
#         fields = ['appointment_id', 'patient', 'doctor', 'date', 'time', 'status', 'reason']
#         read_only_fields= ['patient'] 

from rest_framework import serializers
from .models import Appointment
from patient.serializers import PatientProfileSerializer  # Create this if not already done
from doctors.serializers import DoctorProfileSerializer, DoctorProfile
from users.serializers import PatientDetailsSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    # Display full patient details using a dedicated serializer (or you could use RegisterSerializer if you prefer)
    patient = PatientDetailsSerializer(read_only=True)
    # patient = serializers.StringRelatedField()
    
    # Display full doctor details (read-only)
    doctor = DoctorProfileSerializer(read_only=True)
    
    # Accept doctor input via doctor_id when creating/updating appointments.
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorProfile.objects.all(), 
        source='doctor', 
        write_only=True
    )

    class Meta:
        model = Appointment
        # Include the doctor_id field for input
        fields = ['appointment_id', 'patient', 'doctor', 'doctor_id', 'date', 'time', 'status', 'reason']
        read_only_fields = ['patient']
