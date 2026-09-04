from django.db import models

# Create your models here.

class Course(models.Model):
    c_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name

class Student(models.Model):

    s_name = models.CharField(max_length=100)
    email = models.EmailField()

    Courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.s_name
    