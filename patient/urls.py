from django.urls import path
from .views import PatientProfileCreateUpdateView, PatientProfileRetrieveView

urlpatterns = [
   
    path('profile/', PatientProfileCreateUpdateView.as_view(), name='patient-profile-create-update'),
    
    path('profile/view/', PatientProfileRetrieveView.as_view(), name='patient-profile-view'),
]
