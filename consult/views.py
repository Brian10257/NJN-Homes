from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices  
from .models import Consult

def consult(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        consult = Consult(name=name, email=email, phone=phone, subject=subject, message=message)
        consult.save()

        # Send Mail
        send_mail(
            'Message Recieved From NJN Homes User Acount.',
            'A Message Has Been Recieve From NJN Websits. Sign into admin panel for more info',
            'ntschangb@gmail.com', 
            ['ntschanb@yahoo.com', 'ntschangb@gmail.com'],
            fail_silently=False
        )

        messages.success(request, ' Your Message Has Been Recieved')
        return redirect('consult')
    
    
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'state_choices': state_choices
    }
    
    return render(request, 'pages/consult.html', context)