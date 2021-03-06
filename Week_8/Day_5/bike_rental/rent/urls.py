from django.urls import path
from . import views



urlpatterns = [
    path('customer/', views.customer, name='customer'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:pk>', views.customer_id, name='customer_id'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('vehicle/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicle/<int:pk>', views.vehicle_id, name='vehicle_id'),
    path('rental/', views.rental, name='rental'),
    path('rental/add/', views.add_rental, name='add_rental'),
    path('rental/<int:pk>', views.rental_id, name='rental_id')


]

