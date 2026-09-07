from django.urls import path
from .import views


urlpatterns = [
    path('register/',views.registration_view),
    path('home/',views.home_view,name = 'home'),
]