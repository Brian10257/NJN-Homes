from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
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
        comments.save()
        
        # Send Mail  
        if request.user.is_authenticated:
            subject= str(request.user) +": Posted A Comment. "
        else:
            subject= "A Visitor:  Posted A Comment. "


        message= name + " With The Email: " + email +" Posted A Comment At NJN HOMES Website: "   "\n\n The Comment Goes As Follows: \n\n" + comment + "\n\n\n Contact The Web Master For More Information On The Comment Posted.";
        send_mail(subject, message, 'wgrealestate21@gmail.com', ['ntschangb@yahoo.com', 'ntschangb@gmail.com'] , [''])

        
        messages.success(request, 'Your Comment Has Been Posted')
        
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
