from django.db import models
from django.conf import settings
from doctors.models import DoctorProfile

# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
    ]
    
    appointment_id = models.AutoField(primary_key=True)
    patient= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments")
    doctor=models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="appointments")
    date= models.DateField()
    time= models.TimeField()
    status=models.CharField(max_length=10 , choices=STATUS_CHOICES, default="pending")
    reason= models.TextField()

    def __str__(self):
        return f" You have an appointment with Dr.{self.doctor} on {self.date} by {self.time}"

