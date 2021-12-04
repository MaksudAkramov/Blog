# from django.shortcuts import render

# # Create your views here.
# from django.http.response import HttpResponse
# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
# from django.shortcuts import redirect, render

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, logout

# from account.forms import RegistrationForm, UserForm
# from .models import Account




# def log_user_in(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#         form = UserForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
            
#             return redirect('home')
#     else:
#         form = UserForm()
#     return render(request, 'account/login.html', context={'form': form, 'next': 'home'})


# def log_user_out(request):
#     if request.user.is_authenticated:
#         logout(request)
#     return redirect('login')


# def register(request):
#     if request.user.is_authenticated:
        
#         return redirect('home')
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             login(request, user)
            
            
#             return redirect('home')
#     else:
#         form = RegistrationForm()
#     return render(request, 'account/register.html', context={'form': form})

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserForm
from django.contrib import messages


def log_user_in(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = UserForm()
    return render(request, 'account/login.html', context={'form':form})


def log_user_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next') or 'home'
        return redirect(next_url)
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.save()
            login(request, user=user)
            messages.success(request, "Registration successful." )
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', context={'form': form})



