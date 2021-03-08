from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required #cheating way

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('add_film/', login_required(views.AddFilm.as_view()), name='AddFilm'), #cheating way
    path('add_director/', views.AddDirector.as_view(), name='AddDirector'),
]