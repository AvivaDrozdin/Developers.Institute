from django.shortcuts import render
from django.http import HttpResponse
from .urls import *
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin  #<- proper way

# Create your views here.

                    #mixins always come before view
class LoginCreateView(LoginRequiredMixin, CreateView): #create own class to require login
    pass

def homepage(request):
    films = Film.objects.all()
    context = {
        'films':films,
    }
    return render(request, 'homepage.html', context)



class AddFilm(LoginCreateView): #can now inherit LoginCreateView to require login! 
    form_class = AddFilmForm
    template_name = 'add_film.html'
    success_url = reverse_lazy('homepage')


#Login required -  properway "Mixin"
class AddDirector(LoginRequiredMixin, CreateView): #option 2 -  same as above 
    form_class = AddDirectorForm
    template_name = 'add_director.html'
    success_url = reverse_lazy('homepage')





#MRO method resolution order - 