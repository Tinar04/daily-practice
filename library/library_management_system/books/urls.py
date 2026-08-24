from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_view ,name='books'),
    path('book_details/<int:book_id>/',views.book_detail_view ,name = 'details'),
    path('historical_fiction/', views.historical_fiction_view,name = 'historical_fiction'),
    path('fantasy/',views.fantasy_view,name = 'fantasy'),
    path('mystery/',views.mystery_view,name = 'mystery'),
    path('romance/',views.romance_view,name = 'romance'),
    path('science_fiction/',views.science_fiction_view,name= 'science_fiction')
]