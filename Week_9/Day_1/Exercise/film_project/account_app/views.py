from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





# Create your views here.

def sign_up(request):
    if request.user_is_authenticated:
        return redirect('homepage')
    else:
        form1 = CreateUserForm()
        if request.method = 'POST':
            form1 = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Welcome' + user)
                #log user in here
                return redirect('homepage')
        
        context = {'form1': form1}
        return render(request, 'sign_up.html', context)



def login(request):
    if request.user_is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, username)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or password incorrect')
        
        context = {}
        return render(request, 'login.html', context)

def logout(request):
    logout(request)
    return('homepage')



    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #        #login after signup
    #         user = authenticate(username=user.username, password=pwd)
    #         login(request, user)

    #     #go to homepage
    #     return redirect('homepage')
        
    # else:
    #     form = SignUpForm()
    # return render (request, 'sign_up.html', {'form': form})
