from django.urls import path
from . import views


urlpatterns = [
    path('',views.login_view,name='login'),
    path('register_user/',views.add_employee_view,name='register'),
    path('logout/',views.logout_view,name='logout'),

]