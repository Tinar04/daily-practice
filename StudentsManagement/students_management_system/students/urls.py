from django.urls import path
from . import views

urlpatterns = [

 path('add/',views.create_students_view),
 path('display_students/',views.display_students_view,name = 'display'),
 path('update_student/<int:student_id>/',views.update_student_view,name = 'update'),
 path('delele_student/<int:student_id>/',views.delete_student_view,name = 'delete'),


 ]                    
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               

                               
                               

                               

