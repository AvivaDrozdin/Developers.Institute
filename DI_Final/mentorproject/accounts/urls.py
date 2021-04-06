from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html', form_class=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('skills/', views.SkillAutocomplete.as_view(), name='skill-autocomplete')
]