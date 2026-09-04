from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Category_name


class Producct(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null = True)