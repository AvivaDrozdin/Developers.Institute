from django.shortcuts import render


# Create your views here.

def searchteacher_view(request):
    pass

def searchstudent_view(request):
    pass

def search_view(request):
    return render(request, 'search/search.html')


