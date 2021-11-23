from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def greet(request):
    return HttpResponse("hi, derrick")

def enock(request):
    return HttpResponse("enock is the front engineer in kenya")

def photos(request):
    return HttpResponse("nude photos are not allowed")

# avoiding too many greetings code

def all_greet(request):
    return HttpResponse ("hi")    