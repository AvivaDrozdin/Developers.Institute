from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import *


# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        super().form_valid(form)

        user = authenticate(self.request, username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'])

    

# def sign_up(request):
#     if request.method == 'POST':
#         form == SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#            #login after signup
#             user = authenticate(username=user.username, password=pwd)
#             login(request, user)

#         #go to homepage
#         return redirect('homepage')
        
#     else:
#         form = SignUpForm()
#     return render (request, 'sign_up.html', {'form': form})
