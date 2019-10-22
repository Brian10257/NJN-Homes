from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator        
from django.contrib import messages
from django.db.models import Q
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices  
from .models import Property_single

def properties(request):
    properties = Property_single.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)

    context = { 
        'properties' : paged_properties,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices,
    }

    return render(request, 'properties/properties.html', context)

 
def property_single(request, property_single_id):
    property_single = get_object_or_404(Property_single, pk= property_single_id) 
     
    context= {
        'property_single': property_single,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices
    }

    return render(request, 'properties/property_single.html', context)

def search(request):
    queryset_list = Property_single.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description1__icontains=keywords)|
                                                 Q(description2__icontains=keywords)|
                                                 Q(property_type__icontains=keywords)|
                                                 Q(title__icontains=keywords)|
                                                 Q(status__icontains=keywords)|
                                                 Q(bedrooms__icontains=keywords)|
                                                 Q(city__icontains=keywords)|
                                                 Q(bathrooms__icontains=keywords)|
                                                 Q(garage__icontains=keywords)|
                                                 Q(amenity1__icontains=keywords)|
                                                 Q(amenity2__icontains=keywords)|
                                                 Q(amenity3__icontains=keywords)|
                                                 Q(amenity4__icontains=keywords)|
                                                 Q(amenity5__icontains=keywords)|
                                                 Q(amenity6__icontains=keywords)|
                                                 Q(amenity7__icontains=keywords)| 
                                                 Q(amenity8__icontains=keywords)| 
                                                 Q(amenity9__icontains=keywords)|
                                                 Q(price__icontains=keywords)|
                                                 Q(area__icontains=keywords)) 
                                                
        
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
            
    # Garage
    if 'garage' in request.GET:
        garage = request.GET['garage'] 
        if garage:
            queryset_list = queryset_list.filter(garage__lte=garage)


    # Price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'price_choices': price_choices,
        'garage_choices': garage_choices,
        'properties': queryset_list,
        'values': request.GET
    }
    return render(request, 'properties/search.html', context)