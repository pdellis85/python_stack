from django.shortcuts import render, redirect
from dojo_ninjas_app.models import Dojo, Ninja

# Create your views here.
def root(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }
    return render(request, "home.html", context)

def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo_id=request.POST['dojo_id.dojo'],
    )
    return redirect('/')