from django.urls import path
from .import views

urlpatterns = [
    path('',views.display_employee_view,name = 'display'),
    path('create_employee/',views.create_employee_view,name= 'create'),
    path('update_employee/<int:emp_id>',views.update_employee_View,name = 'update'),
    path('delete_exmployee/<int:emp_id>',views.delete_employee_view,name = 'delete'),
    # path('update_task/<int:task_id>',views.update_task_view,name ='update'),
]