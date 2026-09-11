from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=100)

    def __str__(self):
        return self.d_name

class Employee(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=[('admin','Admin'),('employee','Employee')])
    department = models.ForeignKey('Department',on_delete=models.PROTECT)


    def __str__(self):
        return self.name

class Profile(models.Model):
    employee = models.OneToOneField('Employee',on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,unique=True)
    address = models.TextField(null = True)
    joining_data = models.DateField()

class Project(models.Model):
    p_name = models.CharField(max_length=100,null = True)
    start_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=20,choices=[('ongoing','ongoing'),('completed','completed')])
    employee = models.ManyToManyField('Employee')

    def __str__(self):
            return self.p_name
    




