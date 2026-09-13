from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.admin_home_view,name='admin-home'),
    path('employee_home/',views.employee_home_view,name='emp-home')
    
]