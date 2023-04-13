from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'DoctorName','EmailAddress','Mobile',
    ]
    pass

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'PatientName','Mobile','Address','Symptoms','AdmitDate','AssignedDoctorId'
    ]
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(PatientDischargeDetails)
class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass

