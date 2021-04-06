from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from dal import autocomplete

# Create your views here.

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})



# def login_view(request):  --------> Notes: Login in urls now! 
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.user_cache)

#             print('login form is valid')
#             return redirect('dashboard')
#     else:
#         form = LoginForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
    return redirect('login')

@login_required
def dashboard_view(request):  
    return render(request, 'accounts/dashboard.html')


@login_required
def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')


class SkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Skill.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs