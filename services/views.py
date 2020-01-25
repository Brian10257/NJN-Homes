from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator        
from django.contrib import messages
from properties.choices import state_choices, bathroom_choices, bedroom_choices, garage_choices, price_choices
from .models import Service




def services(request):
    services = Service.objects.order_by('-upload_date')

    paginator = Paginator(services, 1)
    page = request.GET.get('page')
    paged_services = paginator.get_page(page)
    
    context ={
        'services':paged_services,    
        'state_choices':state_choices,
        'bathroom_choices':bathroom_choices,
        'bedroom_choices':bedroom_choices,
        'garage_choices':garage_choices,
        'price_choices':price_choices,
        'values': request.GET,
    }
    
    return render (request, 'pages/services.html', context)