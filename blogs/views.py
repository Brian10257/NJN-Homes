from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    return render(request, 'blogs/blogs.html')

def blog(request):
    return render(request, 'blogs/blog.html')