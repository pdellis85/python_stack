from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print("you created a blog post")
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}" )

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
   return HttpResponse(f"This is a placeholder to delete blog: {number}")