from django.db import models 

# Create your models here.

class Students(models.Model):
    name   = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    marks = models.FloatField()
    subject = models.CharField(max_length=50)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.name


