from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    DoctorName =models.CharField(max_length=20)
    EmailAddress = models.EmailField(unique=True)
    Mobile = models.CharField (max_length=20 ,null=False) 
    status=models.BooleanField(default=False)


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    PatientName = models.CharField(max_length=40)
    Address = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=20,null=False)
    Symptoms = models.TextField(max_length=400,null=False)
    AssignedDoctorId = models.PositiveIntegerField(null=True)
    AdmitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)
    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)
    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)



