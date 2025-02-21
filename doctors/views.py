from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer



class DoctorProfileCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Automatically return the logged-in doctor's profile
        if self.request.user.role != 'doctor':
            raise ValidationError("Only doctors can manage profiles.")
        try:
            return self.request.user.doctor_profile
        except DoctorProfile.DoesNotExist:
            return None  # Let the create action handle profile creation

    def perform_create(self, serializer):
        if self.request.user.role != 'doctor':
            raise ValidationError("Only doctors can create a profile.")
        # If a profile already exists, don't allow creation
        if hasattr(self.request.user, 'doctor_profile'):
            raise ValidationError("Profile already exists. Use update instead.")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.role != 'doctor':
            raise ValidationError("Only doctors can update their profile.")
        serializer.save()

class DoctorProfileListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.AllowAny] 
    filter_backends = [SearchFilter]
    search_fields = ['name', 'specialty']
