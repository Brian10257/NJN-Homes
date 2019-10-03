from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.contrib import messages
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices  
 
from .models import Property_single

def properties(request):
    properties = Property_single.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)

    context = {
        'propeties' : paged_properties
    }

    return render(request, 'properties/properties.html', context)

def property_single(request, property_single_id):
    property_single = get_object_or_404(Property_single, pk= property_single_id) 
     
    context= {
        'property_single': property_single
    }

    return render(request, 'properties/property_single.html', context)

def search(request):
    queryset_list = Property_single.objects.order_by('-list_date')

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