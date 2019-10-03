from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib import messages
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from properties.models import Property_single
from agents.models import Agent
from about.models import About
from properties.models import Property_single

def index(request,):
    properties = Property_single.objects.order_by('-list_date').filter(is_published = True) [:3]
    agents = Agent.objects.order_by('-hire_date')
    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page) 

    context = {
        'properties' : paged_properties
    }
    
    context = {
        'properties' : properties,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'price_choices': price_choices,
        'agents': agents
    }

    return render (request, 'pages/index.html', context )

