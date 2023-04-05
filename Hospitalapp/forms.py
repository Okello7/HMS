from .models  import Doctor , Patient,Appointment,PatientDischargeDetails
from django.forms import ModelForm

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('__all__')

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')      


class ApointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('__all__')

class PatientDischargeDetailsForm(ModelForm):
    class Meta:
        model = PatientDischargeDetails
        fields = ('__all__')      
