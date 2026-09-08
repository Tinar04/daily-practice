from django.db import models

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.d_name

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.name

class Profile(models.Model):
    employee = models.OneToOneField('EmployeeModel',on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null = True,unique=True)
    address = models.TextField(null = True)
    joining_data = models.DateField(null=True)

class Project(models.Model):
    p_name = models.CharField(max_length=100,null = True)
    deadline = models.DateField(null = True)
    empployee = models.ManyToManyField('EmployeeModel')




