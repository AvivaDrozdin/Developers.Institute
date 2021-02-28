from django.shortcuts import render
from django.http import HttpResponse 
import json
with open ('animals.json') as f:
    data = json.load(f)


# Create your views here.

def family(request):
    family_list = data['families']

    return HttpResponse(family_list)



def animals(request):
    animal_list = data['animals']

    return HttpResponse(animal_list)
