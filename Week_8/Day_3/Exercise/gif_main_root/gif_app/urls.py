from django.urls import path
from . import views

urlpatterns = [
    path('all_gifs/', views.all_gifs, name='all_gifs'),
    path('politicians/', views.politicians, name='politicians'),
    path('pets/', views.pets, name='pets'),
    path('friends/', views.friends, name='friends')
]