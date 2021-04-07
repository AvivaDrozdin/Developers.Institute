from django.urls import path
from . import views



urlpatterns = [
    path('searchteachers/', views.searchteacher_view, name='searchteacher'),
    path('searchstudents/', views.searchstudent_view, name='searchstudent'),
    path('search/', views.search_view, name='search'),
    path('results/', views.results_view, name='result'),
]