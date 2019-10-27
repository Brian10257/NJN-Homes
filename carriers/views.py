from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator        
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.db.models import Q
from django.views.generic import ListView
from carriers.choices import job_title_choices, experience_choices
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices
from .models import Carrier, Apply
from .forms import ApplyModelForm
from team.models import Team

def carriers(request):
    carriers = Carrier.objects.order_by('-date_posted').filter(is_published = True)[:6]
    team = Team.objects.order_by('-date_posted') 
    
    context = {
        'team':team,    
        'carriers': carriers,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices, 
        'price_choices': price_choices,
        'experience_choices': experience_choices,
        'job_title_choices': job_title_choices
    }
    
    return render(request, 'carriers/carriers.html', context)


def carrier(request, carrier_id):
    carrier = get_object_or_404(Carrier, pk= carrier_id)
    
    if request.method == 'POST':
        file_form = ApplyModelForm(request.POST, request.FILES)  
        files = request.FILES.getlist('docs')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        place_of_origin = request.POST['place_of_origin']
        current_city = request.POST['current_city']
        neighbour_hood = request.POST['neighbour_hood']
        current_employment = request.POST['current_employment']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if file_form.is_valid():
            for f in files: 
                files = Apply(docs=f, name=name, email=email, phone=phone, place_of_origin=place_of_origin, current_city=current_city, current_employment=current_employment, neighbour_hood=neighbour_hood, message=message, user_id=user_id)
                files.save(send_mail)
                
        # Send Mail  
        if request.user.is_authenticated:
            subject= str(request.user) + " Sent A Job Application On The  NJN HOMES Web Service"
        else:
            subject= "A Visitor Sent A Job Application On The NJN HOMES Web Service"


        message= name + " With The Email: " + email +" And Phone Number: "+phone+ ", Deposited A Job Application For The Position Of: " +str(carrier)+ "\n\n" + message+ "\n\n\n Contact The Web Master For More Information On This Applicaton And Also To Access The Applicant's Files.";
        send_mail(subject, message, 'wgrealestate21@gmail.com', ['ntschangb@yahoo.com', 'ntschangb@gmail.com'] , [email])

        
        messages.success(request, ' Your Application Has Been Recieved. We\'ll get back to you latter')
        
        
    context = {
        'carrier': carrier,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices, 
        'price_choices': price_choices,
        'experience_choices': experience_choices,
        'job_title_choices': job_title_choices
    }
    
    return render(request, 'carriers/carrier.html', context)
    
def jobs(request):
    carriers = Carrier.objects.order_by('-date_posted').filter(is_published = True) 
    paginator = Paginator(carriers, 6)
    page = request.GET.get('page')
    paged_carriers = paginator.get_page(page)
    
    context={
        'carriers': paged_carriers,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices, 
        'price_choices': price_choices,
        'experience_choices': experience_choices,
        'job_title_choices': job_title_choices
    }
    
    return render(request, 'carriers/jobs.html', context)


def search2(request):
    queryset_list = Carrier.objects.order_by('-date_posted')
    
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(company__icontains=keywords)|
                                                 Q(about_job__icontains=keywords)|
                                                 Q(job_available__icontains=keywords)|
                                                 Q(address__icontains=keywords)|
                                                 Q(experience__icontains=keywords)|
                                                 Q(job_title__icontains=keywords)|
                                                 Q(date_posted__icontains=keywords)|
                                                 Q(responsibility_intro__icontains=keywords)|
                                                 Q(responsibility1__icontains=keywords)|
                                                 Q(responsibility2__icontains=keywords)|
                                                 Q(responsibility3__icontains=keywords)|
                                                 Q(responsibility4__icontains=keywords)|
                                                 Q(responsibility5__icontains=keywords)|
                                                 Q(responsibility6__icontains=keywords)|
                                                 Q(responsibility7__icontains=keywords)|
                                                 Q(responsibility8__icontains=keywords)|
                                                 Q(responsibility9__icontains=keywords)|
                                                 Q(responsibility10__icontains=keywords)|
                                                 Q(qualification_intro__icontains=keywords)|
                                                 Q(qualification1__icontains=keywords)|
                                                 Q(qualification2__icontains=keywords)|
                                                 Q(qualification3__icontains=keywords)|
                                                 Q(qualification4__icontains=keywords)|
                                                 Q(qualification5__icontains=keywords)|
                                                 Q(qualification6__icontains=keywords)|
                                                 Q(qualification7__icontains=keywords)|
                                                 Q(qualification8__icontains=keywords)|
                                                 Q(qualification9__icontains=keywords)|
                                                 Q(qualification10__icontains=keywords)|
                                                 Q(employer__icontains=keywords))
                                                
            
    # Experience
    if 'experience' in request.GET:
        experience = request.GET['experience']
        if experience:
            queryset_list = queryset_list.filter(experience__lte=experience)
            
    # Job Title
    if 'job_title' in request.GET:
        job_title = request.GET['job_title']
        if job_title:
            queryset_list = queryset_list.filter(job_title__iexact=job_title)
    
    context = {
        'carriers': queryset_list,
        'values': request.GET,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices, 
        'price_choices': price_choices,
        'experience_choices': experience_choices,
        'job_title_choices': job_title_choices
    }
    
    
    return render(request, 'carriers/search2.html', context)