from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AppointmentStatusUpdateView, AppointmentCancellationView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:pk>/update-status/', AppointmentStatusUpdateView.as_view(), name='appointment-update-status'),
    path('<int:pk>/cancel/', AppointmentCancellationView.as_view(), name='appointment-cancel'),
]



