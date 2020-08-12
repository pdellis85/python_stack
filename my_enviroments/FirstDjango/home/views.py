from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def contact(request):
    return HttpResponse("Contact Me!")


def about(request):
    return HttpResponse("More about me here!!")


def colors(request, name):
    converted = name[0].upper() + name[1:]
    return HttpResponse(f"{converted} is a great color!")


def users(request, id):
    return HttpResponse(f"Page for User # {id} ")
