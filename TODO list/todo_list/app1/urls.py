from django.urls import path
from . import views 

urlpatterns = [
    path('',views.task_form_view,name = 'task_form'),
]