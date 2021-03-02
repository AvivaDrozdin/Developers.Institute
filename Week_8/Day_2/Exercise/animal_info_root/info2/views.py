from django.shortcuts import render
from info2.models import Families, Animals
from django.http import HttpResponse 

# Create your views here.
def family(request, id):
    animals = Animals.objects.filter(family=id)
    context = {
        'content':animals
        #key     value
    }
    return render(request, 'family.html', context)


def animals(request, id):
    animals = Animals.objects.filter(id=id)
    context = {
        'content':animals
    }
    return render(request,'animal.html', context)

def all_animals(request):
    all_animals = Animals.objects.all()
    # link = str(f'../animal/{all_animals[i].id}')
    # for i in range(len(all_animals)):
    #     all_animals[i].link = str(f'../animal/{all_animals[i].id}')
    

    context = {
        'content':all_animals
    }
    return render(request, 'all_animals.html', context)
    




