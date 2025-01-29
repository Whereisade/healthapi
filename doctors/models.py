from django.db import models
from django.conf import settings

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_profile")
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
