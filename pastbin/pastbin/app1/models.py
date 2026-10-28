from django.db import models

# Create your models here.
class Link(models.Model):
    code = models.CharField(max_length=6,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(null=True, blank=True)

