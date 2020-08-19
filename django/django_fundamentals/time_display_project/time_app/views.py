
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        #"date": strftime("%Y-%m-%d"),
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M %p", gmtime())

    }
    return render(request,'index.html', context)


