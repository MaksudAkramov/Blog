from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from account.forms import RegistrationForm
from .models import Account




def log_user_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', context={'form': form, 'next': 'home'})


def log_user_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            login(request, user)
            
            
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', context={'form': form})



