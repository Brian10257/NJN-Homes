from django.shortcuts import render, redirect
from django.contrib import messages, auth
from properties.choices import price_choices, bedroom_choices, bathroom_choices, garage_choices, state_choices
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method== 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                 # Looks Good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect ('register')
      
    else:
        
        context = {
            'price_choices': price_choices,
            'state_choices': state_choices,
            'bedroom_choices': bedroom_choices,
            'bathroom_choices':bathroom_choices,
            'garage_choices': garage_choices
    }
        return render (request, 'accounts/register.html', context)


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
    
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful. Happy Browsing')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials: Please Verify You Entered The Correct Infomation.')
            return redirect('login')
    else:
        context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'garage_choices': garage_choices
    }
        return render (request, 'accounts/login.html', context)
    
    
    


def logout(request):
     if request.method == 'POST':
         auth. logout(request)
         messages.success(request, 'You are now logged out')
         return redirect ('login')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'bathroom_choices': bathroom_choices,
        'garage_choices': garage_choices,
        'price_choices': price_choices
    }
    return render (request, 'accounts/dashboard.html', context)