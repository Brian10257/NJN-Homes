from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices          
from agents.models import Agent
from about.models import About


def about(request):
    about = Agent.objects.order_by('-hire_date')
    paginator = Paginator(about, 6)
    page = request.GET.get('page')
    paged_about = paginator.get_page(page)
    
    # Get MVP 
    mvp_agents = Agent.objects.all().filter(is_mvp = True)

    agents = Agent.objects.all()
    paginator = Paginator(agents, 1)
    page = request.GET.get('page')
    paged_agents = paginator.get_page(page)

    context= {
        'agents': agents,
        'mvp_agents': mvp_agents,
        'agents' : paged_agents,
        'about' : paged_about
    }
    
    return render (request, 'pages/about.html')  
 