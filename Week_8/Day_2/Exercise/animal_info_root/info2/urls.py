from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:id>', views.family, name='family'),
    path('animals/<int:id>', views.animals, name='animals'),
    path('all_animals/', views.all_animals, name='all_animals')
]