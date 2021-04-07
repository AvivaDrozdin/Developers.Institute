from dal import autocomplete
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile 
from .filters import *
from accounts.models import Skill

# Create your views here.



@login_required
def searchteacher_view(request):
    f = ProfileFilterStudentside(request.GET, queryset=Profile.objects.filter(profile_type = 1))
    return render(request, 'search/searchteacher.html', {'f': f})

@login_required
def searchstudent_view(request):
    f = ProfileFilterTeacherside(request.GET, queryset=Profile.objects.filter(profile_type = 2))
    return render(request, 'search/searchstudent.html', {'f': f})
    
@login_required
def search_view(request):
    f = ProfileFilter(request.GET, queryset=Profile.objects.all())
    return render(request, 'search/search.html', {'f': f})


@login_required
def results_view(request):
    return render(request, 'search/results.html')

#