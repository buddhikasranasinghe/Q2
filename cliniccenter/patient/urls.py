from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add_patient, name='addpatient'),
    path('prescription/', views.add_prescription, name='prescription'),
    path('patientdetails/', views.patient_details, name='details'),
    path('revenue/', views.revenue_details, name='revenue'),
]
