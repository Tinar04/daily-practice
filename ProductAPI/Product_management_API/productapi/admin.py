from django.contrib import admin
from .models import Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity','brand']
    search_fields = 'name'

admin.site.register(Products)


