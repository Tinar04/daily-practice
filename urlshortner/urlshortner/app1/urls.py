from django.urls import path
from . import views
urlpatterns = [
    path('shorten/', views.generateUrl ),
    path("<str:code>/", views.redirect_to_og),
]