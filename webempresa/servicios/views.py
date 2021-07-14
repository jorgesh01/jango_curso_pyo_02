from django.shortcuts import render
from .models import Service


# Create your views here.

def services(request):
    services = Service.objects.all()
    html = "<html><body>We're in services<body></html>"
    return render(request,"servicios/services.html",{'services':services})