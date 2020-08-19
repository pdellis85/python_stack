from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    print("you created a blog post")
    return redirect('/')

def show(request, number):
    context = {
        'blog_id': number
    }
    return render(request, 'one_blog.html', context)

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
   return HttpResponse(f"This is a placeholder to delete blog: {number}")