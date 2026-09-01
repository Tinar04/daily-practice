from django.db import models

# Create your models here.
class Task_Model(models.Model):
    status = [
        ("completed",'completed'),
        ("pending",'pending'),
        ("Delayed",'Delayed')
    ]
    
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(null = True)
    status = models.CharField(max_length=15,choices=status, null=True)


    