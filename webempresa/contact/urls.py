from django.urls import path
from . import views 
from django.conf import settings



urlpatterns = [
    #path del core   
    path('', views.contact, name="contactanos"),
   

]

