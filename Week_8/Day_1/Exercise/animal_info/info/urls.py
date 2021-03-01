from django.urls import path
from . import views

urlpatterns = [
    path('all/', view.all_animals, name='all_animals')
    # path('family/', views.family, name='family'),
    # path('animals/', views.animals, name='animals')
]