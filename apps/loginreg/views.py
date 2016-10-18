from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/success')
    else:
        return render(request, 'loginreg/index.html')

def login(request):
    if request.method == 'POST':
        validation = User.objects.login(request.POST)
        if validation[0]:
            print(validation[1].first_name)
            return log_user_in(request, validation[1])
            # messages.success(request, "Successfully logged in")
            # return redirect('/success')
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
            return log_user_in(request, validation[1])
        else:
            for error in validation[1]:
                # add errors to flash messages
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in")
        return redirect('/')
    else:
        context = {
            'users': User.objects.all()
        }
        return render(request, 'loginreg/success.html', context)

def log_user_in(request, user):
    print("running log_user_in function")
    request.session['user_id'] = user.id
    # add user to success flash message
    messages.success(request, user.email)
    return redirect('/success')

def logout(request):
    del request.session['user_id']
    return redirect('/')
