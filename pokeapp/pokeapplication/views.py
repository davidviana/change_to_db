from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("shhh calado")

async def currentdate(request):
    html = "<button>Home</button>."
    return HttpResponse(html)