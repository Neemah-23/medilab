
from django.contrib import admin
from django.urls import path
from MedilabApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('patient/', views.patient, name='patient'),
]
