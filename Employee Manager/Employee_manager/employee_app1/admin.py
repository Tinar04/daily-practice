from django.contrib import admin
from .models import Department,Employee,Profile,Project

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['d_name']
    fields = ['name', 'salary', 'email', 'role', 'department', 'user']
admin.site.register(Department)

class EmloyeeAdmin(admin.ModelAdmin):
    search_fields = ['e_name']
admin.site.register(Employee)

class ProfileAdmin(admin.ModelAdmin):
    ...
admin.site.register(Profile)

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['p_name']

admin.site.register(Project)