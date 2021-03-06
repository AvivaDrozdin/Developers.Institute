from django.urls import path
from . import views



urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('<slug:slug>', views.articles_detail, name ='article_detail')
]

