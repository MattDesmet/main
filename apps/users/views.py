from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def login_page(request):
    return render(request, 'users/login_page.html')

def register(request):
    res = User.objects.register(request.POST)

    if res['added']:
        #add to session at some point
        messages.success(request, 'Added user #{}'.format(res['new_user'].id))
    else:
        for error in res['errors']:
            messages.error(request, error)

    return redirect('users:login_page')

def login(request):
    #logic to be added here
    return redirect('users:login_page')
