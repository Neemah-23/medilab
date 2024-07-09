from django.shortcuts import render,redirect
from MedilabApp.models import Company,Patient

# Create your views here.
def index(request):
    return render(request,'index.html')
def start(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'About.html')
def services(request):
    return render(request,'services.html')
def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    if request.method == 'POST':
        contacts = Company(name =request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'])
        contacts.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')

def patient(request):
    if request.method == 'POST':
        patients = Patient(name =request.POST['name'],
                           emailaddress=request.POST['email'],
                           medicalhistory=request.POST['medicalhistory'],
                           age=request.POST['age'],)

        patients.save()
        return redirect('/patient')

    else:
        return render(request,'patient.html')