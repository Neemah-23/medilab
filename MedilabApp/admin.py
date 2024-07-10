from django.contrib import admin
from MedilabApp.models import Product
from MedilabApp.models import Student
from MedilabApp.models import Patient,Company,Appointment

# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Patient)
admin.site.register(Company)
admin.site.register(Appointment)
