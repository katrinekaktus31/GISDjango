from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    return render(request, "gis/home.html")


# generated for this request some templates
def about(request):
    return render(request, "gis/about.html")
