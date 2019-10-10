from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.contrib import messages
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices  
 
from .models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-date_published') 
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs' : paged_blogs
    }

    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id) 
     
    context= {
        'blog': blog
    }

    return render(request, 'blogs/blog.html', context)

def search(request):
    queryset_list = Blog.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            
    # Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'properties': queryset_list,
        'values': request.GET
    }
    return render(request, 'properties/search.html', context)