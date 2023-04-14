from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'DoctorName','emailAddress','mobile', 'status',
    )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
    'user','PatientName','address','mobile','symptoms','assignedDoctorId','admitDate','status',
    
    
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
    'patientId','doctorId','patientName','doctorName','appointmentDate','description','status',
    
    
    
    )


@admin.register(PatientDischargeDetails)
class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    list_display = (
    
    'patientId','patientName','assignedDoctorName','address','mobile','symptoms','admitDate',
    'releaseDate','daySpent','roomCharge','medicineCost','doctorFee','OtherCharge','total',
    
    )

