from django.urls import path
from .views import signup,signin,signout,home,add_doctor, add_patient,add_DischargeDetails,add_appointment
 
urlpatterns = [
    path('home/', home, name='home'),
    path('doctor/', add_doctor, name='Doctor'),
    path('patient/', add_patient, name='Patient'),
    path('appointment/', add_appointment, name='Appointment'),
    path('discharge/', add_DischargeDetails, name='Discharge'),
    path('home/signup/', signup, name ='signup'),
    path('home/signin/', signin, name = 'login'),
    path('home/signout/', signout, name = 'logout'),
]