from django.contrib import admin
from .models import Students

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    search_fields = ["name"]
admin.site.register(Students)