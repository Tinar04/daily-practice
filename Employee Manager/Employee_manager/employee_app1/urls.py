from django.urls import path
from .import views

urlpatterns = [
    path('display_employee',views.display_employee_view),
    path('add_employee/',views.add_employee_view,name='add_employee'),
    path('update_employee/<int:emp_id>',views.update_employee_view,name='update'),
    path('delete_employee/<int:emp_id>',views.delete_employee_view,name='delete'),
    
]