from django.shortcuts import get_object_or_404, render
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices         
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Agent
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def agents(request):
    # Get all agents
    agents = Agent.objects.order_by('-hire_date')
    paginator = Paginator(agents, 6)
    page = request.GET.get('page')
    paged_agents = paginator.get_page(page)
    
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
        'agents' : paged_agents
    }
    
    return render (request, 'agents/agents.html', context)  

def agent(request, agent_id):
    agent = get_object_or_404(Agent, pk= agent_id) 
     
    context= {
        'agent': agent
    }

    return render(request, 'agents/agent.html', context)
