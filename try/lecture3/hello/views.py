from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,name):
    return render(request, "hello/index.html", {
        "name": name
    })

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

def enock(request):
    return HttpResponse("enock is the front engineer in kenya")

def photos(request):
    return HttpResponse("nude photos are not allowed")

# avoiding too many greetings code

# def all_greet(request, name):
#     return render(request, "hello/greet.html", {
#         "name":name.capitalize()
#     })    