from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

class DoctorProfileCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "doctor":
            raise ValidationError("Only doctors can create a profile.")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.role != "doctor":
            raise ValidationError("Only doctors can update their profile.")
        serializer.save()

class DoctorProfileListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.AllowAny] 
    filter_backends = [SearchFilter]
    search_fields = ['name', 'specialty']
