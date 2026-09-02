from django.db import models

# Create your models here.

Department = [
    ("AI/ML",'artificial intelligence & Machine Learning'),
    ("DS & Research", 'Data science and research department'),
    ("HR & manager","HUman Resource & Manager"),
    ("Interns & JEs",'Interns & Junior Enigneers'),
]
class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100,null = True,choices=Department)
    salary = models.FloatField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


