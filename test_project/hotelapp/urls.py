from django.db import router
from django.urls import path,include
from . import views
from .utility import *

urlpatterns = [
    path('',views.home),
    path('add/',views.AddView),
    path('fetch_name/',views.Restaurantview),
    path('delete/id=<str:inp>/',views.DeleteView),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]