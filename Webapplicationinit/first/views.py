from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  render(request, "first/index.html")

def greet(request, name):
    return render(request, "first/greet.html", {
        "name" : name.capitalize()
    })
