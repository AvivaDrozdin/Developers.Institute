from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
           #login after signup
            user = authenticate(username=user.username, password=pwd)
            login(request, user)

        #go to homepage
        return redirect('homepage')
        
    else:
        form = SignUpForm()
    return render (request, 'sign_up.html', {'form': form})
