from django.urls import path
from . import views

urlpatterns = [
    path('',views.display_course_view),
    path('details/<str:code_id>',views.details_of_course_view,name='details'),
]