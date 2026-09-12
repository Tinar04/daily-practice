from django.urls import path
from . import views


urlpatterns = [
    path('',views.products_list_view,),  #get,post
    path('<int:product_id>',views.products_details_view), # get patch,put
]