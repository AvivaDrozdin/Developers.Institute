from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = 'homepage'

    def form_valid(self, form):
        super().form_valid(form)

        user = authenticate(self.request, username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'])

        login(self.request, user)

        return redirect(reverse(self.get_success_url()))


    
class LoginView(LoginView):
    template_name = 'login.html'
    pass

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect ('login')

def profile_view(request, pk):
    user_profile = User.objects.get(id=pk)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)
