from django.shortcuts import render, redirect

# Create your views here.


def root(request):
    return render(request, "home.html")
