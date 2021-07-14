from django.urls import path
from . import views 
from django.conf import settings



urlpatterns = [

    path('<int:page_id>/<slug:page_slug>/',views.page, name="page"),   

]
