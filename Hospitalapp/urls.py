from django.urls import path
from . import views #signup,signin,signout,home,add_doctor, add_patient,add_DischargeDetails,add_appointment
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('doctor/', views.add_doctor, name='Doctor'),
    path('patient/', views.add_patient, name='Patient'),
    path('appointment/', views.add_appointment, name='Appointment'),
    path('discharge/', views.add_DischargeDetails, name='Discharge'),
    path('signup/', views.signup, name ='signup'),
    path('signin/', views.signin, name = 'login'),
    path('signout/', views.signout, name = 'logout'),
    
]