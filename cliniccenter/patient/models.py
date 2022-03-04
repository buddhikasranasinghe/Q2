from django.db import models

# Create your models here.
class Patient(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    birthday = models.DateField()
    contactno = models.IntegerField()
    photo = models.CharField(max_length=100)
    nic = models.CharField(max_length=20)
    notes = models.CharField(max_length=500)
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=500)
    amount = models.FloatField()
    date = models.DateField()