from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile 
from .filters import ProfileFilter

# Create your views here.

@login_required
def searchteacher_view(request):
    #see below filter teacher
    return render(request, 'search/searchteacher.html')

@login_required
def searchstudent_view(request):
    #see below filter student
    return render(request, 'search/searchstudent.html')
    
@login_required
def search_view(request):
    f = ProfileFilter(request.GET, queryset=Profile.objects.all())
    return render(request, 'search/search.html', {'f': f})

@login_required
def results_view(request):
    return render(request, 'search/results.html')

