from django.shortcuts import render, get_object_or_404 #get object or 404 checks database for an object. Returns the object or a 404 if DNE
from .models import Blog

# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id): #receives the int the user requested after the /blog/ as blog_id
    detailblog = get_object_or_404(Blog, pk=blog_id) #parameters are type of object and primary key - how to look it up in db
    return render(request, 'blog/detail.html', {'blog': detailblog})
