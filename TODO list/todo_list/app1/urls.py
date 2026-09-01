from django.urls import path
from . import views 

urlpatterns = [
    path('',views.task_form_view,name = 'task_form'),
    path('update_task/<int:task_id>',views.update_task_view,name ='update'),
    path('delete_task/<int:task_id>',views.delete_task_view,name='delete')
]