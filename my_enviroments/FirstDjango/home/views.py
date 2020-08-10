from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def contact(request):
    return HttpResponse("Contact Me")

def about(request):
    return HttpResponse("More about me here!")