from django.db import models
from django.conf import settings

class PatientProfile(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='patient_profile'
    )
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.email})"
