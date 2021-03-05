from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def articles(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles.html', {'content': articles})