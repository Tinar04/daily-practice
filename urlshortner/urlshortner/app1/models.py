from django.db import models

# Create your models here.
class Links(models.Model):
    original_url = models.URLField()
    code = models.CharField(max_length=6,unique=True)
    clicks = models.IntegerField(default=0)

    