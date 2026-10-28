from django.urls import path
from . import views

urlpatterns = [
    path("get-url/",views.generate_link ),
    path("<str:code>/",views.get_message)
]