from django.urls import path
from .views import DoctorProfileCreateUpdateView, DoctorProfileListView

urlpatterns = [
    path('', DoctorProfileListView.as_view(), name='doctor-list'),
    path('manage/', DoctorProfileCreateUpdateView.as_view(), name='doctor-create-update'),
]
