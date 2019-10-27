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
        if request.user.is_authenticated:
            subject= str(request.user) +': '+ subject
        else:
            subject= "A Visitor: "+subject 


        message= name + " With The Email: " + email +", And Phone Number: "+phone+", Sent The Following Message:\n\n" + message+"\n\n Please Do Reply Promtly.";
        send_mail(subject, message, ['wgrealestate21@gmail.com'], ['ntschangb@yahoo.com', 'ntschangb@gmail.com'] , [email])


        messages.success(request, ' Your Message Has Been Recieved. We\'ll get back to you latter')
        return redirect('consult')
    
    
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'state_choices': state_choices
    }
    
    return render(request, 'pages/consult.html', context)