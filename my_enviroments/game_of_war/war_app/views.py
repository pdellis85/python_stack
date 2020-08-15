from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home.html')

def game(request):
    #store player data (to customize game experience)
    
    #return will redirect to a method that renders game.html
    return render(request, 'home.html')