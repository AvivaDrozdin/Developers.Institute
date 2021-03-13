from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin # <- mixin allows login required on classes
import json

# Create your views here.

def homepage(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'homepage.html', context)

class AddFilm(LoginRequiredMixin, CreateView):
    form_class = AddFilmForm
    template_name = 'addfilm.html'
    success_url = reverse_lazy('homepage')
    

class AddDirector(LoginRequiredMixin, CreateView):
    form_class = AddDirectorForm
    template_name = 'adddirector.html'
    success_url = reverse_lazy('homepage')

