from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from properties.views import *

def contact(request):
    if request.method == 'POST':
        property_single_id = request.POST['property_single_id']
        property_single = request.POST['property_single']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message'] 
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']

        # Check if User has Made Inquiry Already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                property_single_id=property_single_id, user_id=user_id)
            if has_contacted:
                messages.error(request, ': You have already submited an inquiry for this particular property')
                return redirect('properties')

        contact = Contact(property_single=property_single, property_single_id=property_single_id,
                          name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send Mail
        send_mail(
            'SUBJECT: An Inquiry On Listed Property',
            'There has been an inquiry for ' + property_single +
            '. Sign into admin panel for more info' "\n\n" 
            "SENDER:  "+ name+ ',' " PHONE NUMBER: "+phone+',' " EMAIL:  "+email+',' " LISTING:  "+ property_single+  "\n\n" 
            "MESSAGE: \n\n " + message,
            'ntschangb@gmail.com',
            [agent_email, 'ntschangb@gmail.com'],
            fail_silently=False
        )

        messages.success(request, ': Your request has been submitted, an Agent will get back to you soon')
        return redirect('properties')
