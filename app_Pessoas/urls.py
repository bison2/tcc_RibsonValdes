from django.urls import path, include 
from .views import home

app_name= 'pessoa_disc'
urlpatterns =[
   
    path('', home),
]