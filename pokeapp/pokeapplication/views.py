from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

x = 24
y = 2

def index(request):
    return HttpResponse(f"Eita boy: {x , y}")