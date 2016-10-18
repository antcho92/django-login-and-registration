from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def login(request):
    if request.method == 'POST':
        validation = User.objects.login(request.POST)
        if validation[0]:
            messages.success(request, "Successfully logged in")
            return redirect('/success')
        else:
            messages.error(request, validation[1])
            return redirect('/')
    else:
        return redirect('/')

def register(request):
    if request.method == 'POST':
        validation = User.objects.register(request.POST)
        #check if registration validation returns true
        if validation[0]:
            # add user to success flash message
            messages.success(request, validation[1].email)
            return redirect('/success')
        else:
            for error in validation[1]:
                # add errors to flash messages
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'loginreg/success.html', context)

def log_user_in(request, user):
    
    return redirect('success')
