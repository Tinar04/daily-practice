from django.urls import path
from .import views

urlpatterns = [
    path('display_employee',views.display_employee_view,name='display_emp'),
    path('add_employee/',views.add_employee_view,name='add_employee'),
    path('update_employee/<int:emp_id>',views.update_employee_view,name='update'),
    path('delete_employee/<int:emp_id>',views.delete_employee_view,name='delete'),


    path('display_department/',views.department_list,name='display_table'),
    path('create_department/',views.create_department,name='create_dept'),
    path('update_department/<int:dept_id>',views.update_department,name='update_dept'),
    path('delete_department/<int:dept_id>',views.delete_department,name='delete_dept'),



    path('create_project/',views.create_project,name='create_project'),
    path('view_one_project/<int:p_id>',views.display_one_project,name='project_detail'),
    path('update_project/<int:p_id>',views.update_project_view,name='update_project'),
    path('delete_project/<int:p_id>',views.delete_project_view,name='delete_project'),

    
]