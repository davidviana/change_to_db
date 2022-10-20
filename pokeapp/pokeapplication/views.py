from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("shhh calado")

def currentdate(request):
    a = 2 + 2
    cars = ["Honda", "Toyota", "Ferrari"]
    context = {"result": a, "cars": cars}

    return render(request, "index.html", context)