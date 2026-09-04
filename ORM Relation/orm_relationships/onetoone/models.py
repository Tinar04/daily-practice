from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name


class Salary_account(models.Model):
    acc_no = models.CharField(max_length=12)
    ifsc = models.CharField(max_length=10)

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)


    def __str__(self):
        return self.acc_no