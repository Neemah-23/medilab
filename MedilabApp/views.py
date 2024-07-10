from django.shortcuts import render,redirect
from MedilabApp.models import Company,Patient,Appointment

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

def appointment(request):
    if request.method == 'POST':
        appointments = Appointment(name=request.POST['name'],
                                   email=request.POST['email'],
                                   message=request.POST['message'],
                                   phone=request.POST['phone'],
                                   department=request.POST['department'],
                                   doctor=request.POST['doctor'],
                                   date=request.POST['date'])

        appointments.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

def show(request):
    data = Appointment.objects.all()
    return render(request,'show.html',{'appointment':data})

def delete(request,id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')