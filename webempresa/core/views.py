from django.shortcuts import render


# Create your views here.

def home(request):
    html = "<html><body>We're in home<body></html>"
    return render(request,"core/home.html")
def about(request):
    html = "<html><body>We're in about<body></html>"
    return render(request,"core/about.html")
def store(request):
    html = "<html><body>We're in store<body></html>"
    return render(request,"core/store.html")
def contact(request):
    html = "<html><body>We're in contact<body></html>"
    return render(request,"core/contact.html")

