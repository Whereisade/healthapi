from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AppointmentStatusUpdateView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:pk>/update-status/', AppointmentStatusUpdateView.as_view(), name='appointment-update-status'),
]



