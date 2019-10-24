from django.shortcuts import render
from properties.choices import state_choices, bathroom_choices, bedroom_choices, garage_choices, price_choices
from properties.models import Property_single

def services(request):
    
    context ={
        'state_choices':state_choices,
        'bathroom_choices':bathroom_choices,
        'bedroom_choices':bedroom_choices,
        'garage_choices':garage_choices,
        'price_choices':price_choices,
        'values': request.GET,
    }
    
    return render (request, 'pages/services.html', context)