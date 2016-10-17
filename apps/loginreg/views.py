from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def login(request):

    return redirect(index)

def register(request):
    if request.method == 'POST':
        result = User.objects.register(request.POST)
        if result[0]:
            # add user to success flash message
            messages.success(request, request.POST['email'])
            return redirect('/success')
        else:
            for error in result[1]:
                # add errors to flash messages
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    return render(request, 'loginreg/sucess.html')
