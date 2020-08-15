from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,'form.html')

def result(request):
    return render(request, 'result.html')