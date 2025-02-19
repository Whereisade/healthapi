from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import PatientProfile
from .serializers import PatientProfileSerializer

# View for creating or updating the patient's profile
class PatientProfileCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        if self.request.user.role != 'patient':
            raise ValidationError("Only patients can create a profile.")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        
        if self.request.user != self.get_object().user:
            raise ValidationError("You can only update your own profile.")
        serializer.save()


class PatientProfileRetrieveView(generics.RetrieveAPIView):
    serializer_class = PatientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        
        try:
            return self.request.user.patient_profile
        except PatientProfile.DoesNotExist:
            raise ValidationError("Patient profile does not exist.")
