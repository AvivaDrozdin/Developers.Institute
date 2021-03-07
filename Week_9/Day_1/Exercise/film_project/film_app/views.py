from django.shortcuts import render
from django.http import HttpResponse
from .urls import *
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.

def homepage(request):
    return render (request, "homepage.html")


class AddFilm(CreateView):
    form_class = AddFilmForm
    template_name = 'add_film.html'
    success_url = reverse_lazy('homepage')

class AddDirector(CreateView):
    form_class = AddDirectorForm
    template_name = 'add_director.html'
    success_url = reverse_lazy('homepage')
