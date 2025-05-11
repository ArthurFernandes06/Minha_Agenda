from django.shortcuts import render
from django.template import loader

def home_views(request):
    return render(request, "home/home.html")
# Create your views here.
