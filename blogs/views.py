from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.contrib import messages
from .models import Blog, Comment


def blogs(request):
    blogs = Blog.objects.order_by('-date_published') 
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs' : paged_blogs,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices, 
        'price_choices': price_choices
    }

    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id) 
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comment = request.POST['comment']
        
        
        comments = Comment(image=image, name=name, email=email, website=website, comment=comment)
        messages.success(request, 'Your comment has been submitted')
        comments.save()

    blogs = Comment.objects.all()
    
    context= { 
        'blog': blog,
        'blogs':blogs,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices,
    }

    return render(request, 'blogs/blog.html', context)
