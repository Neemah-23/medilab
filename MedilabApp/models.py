from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
      fullname = models.CharField(max_length=200)
      email = models.EmailField()

      def __str__(self):
          return self.fullname

# fullname,email,medicalhistory,age

class Patient(models.Model):
      name = models.CharField(max_length=200)
      emailaddress = models.EmailField()
      medicalhistory = models.TextField()
      age = models.IntegerField()


      def __str__(self):
          return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=10)
    staff = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=10)
    doctor = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    date = models.DateField()


    def __str__(self):
        return self.name



class Member(models.Model):
        name = models.CharField(max_length=200)
        username = models.CharField(max_length=200)
        password = models.CharField(max_length=200)

        def __str__(self):
            return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Admin(models.Model):
   username = models.CharField(max_length=50)
   password = models.CharField(max_length=50)

   def __str__(self):
       return self.username


