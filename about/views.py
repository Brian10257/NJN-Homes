from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices          
from agents.models import Agent
from .models import About


def about(request): 
    about = About.objects.all()
    
    # Get MVP 
    mvp_agents = Agent.objects.all().filter(is_mvp = True)

    agents = Agent.objects.all() [:3]

    

    context= {
        'mvp_agents': mvp_agents,
        'about' : about, 
        'agents': agents,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices 
    }
    
    return render (request, 'pages/about.html', context)  
 