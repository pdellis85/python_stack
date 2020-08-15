from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,'form.html')

def result(request):
    return render(request, 'result.html')

def create(request):
    request.session['name'] = request.POST['fname']
    request.session['city'] = request.POST['location']
    request.session['lang'] = request.POST['language']
    request.session['comms'] = request.POST['comment']
    return redirect('/')

