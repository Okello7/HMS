from django.shortcuts import render , redirect
from .forms import DoctorForm, PatientForm,Appointment,PatientDischargeDetails
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
# Create your views here.
#Replaced all redirects to /home with https://www.example.com/
# to find out the prob redirecting to hone

def add_doctor(request):
    form = DoctorForm
    return render(request,'Doctor.html', {'form':form})

def add_patient(request):
    form = PatientForm
    return render(request,'Patient.html', {'form':form})

def add_appointment(request):
    form = Appointment
    return render(request,'Appointment.html', {'form':form})

def add_DischargeDetails(request):
    form = PatientDischargeDetails
    return render(request,'Discharge.html', {'form':form})

def home(request):
    texts = "Here is my First Home"
    return render(request,'home.html',{"trial":texts})


    

 
def signup(request):
 
    if request.user.is_authenticated:
        return redirect('https://www.example.com/')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('https://www.example.com/')
         
        else:
            return render(request,'signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
    
def signin(request):
    if request.user.is_authenticated:
        return redirect('https://www.example.com/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('https://www.example.com/')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
 
def signout(request):
    #logout(request)
    return redirect('/home')

# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         return redirect('/hospital/home')
#     #form = PatientDischargeDetails
#     #return render(request,'Discharge.html', {'form':form})
    