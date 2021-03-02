from django.shortcuts import render
from gif_app.models import Gif, Category
from django.http import HttpResponse 

# Create your views here.
def all_gifs(request):
    gifs = Gif.objects.all()
    context = {
        'gifs':gifs
        #key     value
    }
    return render(request, 'all_gifs.html', context)


def politicians(request):
    poli = Category.objects.filter(id=1)
    context = {
        'gifs': poli
    }
    return render(request,'politicians.html', context)

def friends(request):
    friends = Category.objects.filter(id=2)
    context = {
        'gifs': friends
    }
    return render(request,'friends.html', context)

def pets(request):
    pets = Category.objects.filter(id=3)
    context = {
        'gifs': pets 
        }
    return render(request,'gif_app/pets.html', context)
