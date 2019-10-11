from django.shortcuts import get_object_or_404, render
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Agent
from properties.models import Property_single
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def agents(request):
    # Get all agents
    agents = Agent.objects.order_by('-hire_date')
    paginator = Paginator(agents, 6)
    page = request.GET.get('page')
    paged_agents = paginator.get_page(page)
    
    # Get Employee Of The Month 
    mvp_agents = Agent.objects.all().filter(is_mvp = True)

    context= {
        'agents': agents,
        'mvp_agents': mvp_agents,
        'agents' : paged_agents,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices
    }

    return render (request, 'agents/agents.html', context)  

def agent(request, agent_id):
    agent = get_object_or_404(Agent, pk= agent_id) 
    properties = Property_single.objects.order_by('-list_date').filter(is_published = True)
    context= {
        'agent': agent,
        'properties' : properties,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices
    }

    return render(request, 'agents/agent.html', context)

