from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "patient":
            raise ValidationError("Only patients can create appointments.")
        serializer.save(patient=self.request.user)


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == "doctor":
            return Appointment.objects.filter(doctor__user=self.request.user)
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        appointment = self.get_object()
        if self.request.user.role != "doctor" or appointment.doctor.user != self.request.user:
            raise ValidationError("Only the assigned doctor can update this appointment.")
        serializer.save()
