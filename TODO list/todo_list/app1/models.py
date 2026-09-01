from django.db import models

# Create your models here.
class Task_Model(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(null = True)

    