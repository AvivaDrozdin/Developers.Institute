from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def customer(request):
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'customer.html', context)

def add_customer(request):
    if request.method == 'GET':
        add_customer = Add_customer()
        return render(request, 'add_cus.html', {'add_customer':add_customer})
    
    if request.method == 'POST':
        add_customer = Add_customer(request.POST)

    if add_customer.is_valid():
        fname = add_customer.cleaned_data['fname']
        lname = add_customer.cleaned_data['lname']
        email = add_customer.cleaned_data['email']
        phone = add_customer.cleaned_data['phone']
        address = add_customer.cleaned_data['address']
        city = add_customer.cleaned_data['city']
        country = add_customer.cleaned_data['country']

        f = Customer(fname=fname, lname=lname, email=email, phone=phone, address=address, city=city, country=country)

        f.save()
    
    else:
        return render(request, 'add_cus.html', {'add_customer':add_customer})


def customer_id(request, pk):
    one_customer = Customer.objects.get(id=pk)
    context = {
        'one_customer':one_customer
    }
    return render(request, 'customer.html', context)


def vehicle(request):
    vehicle = Vehicle_type.objects.all()
    context = {
        'vehicle':vehicle
    }
    return render(request, 'vehicle.html', context)


def add_vehicle(request, pk):
    pass

def vehicle_id(request, pk):
    one_vehicle = Vehicle.objects.get(id=pk)
    context = {
        'one_vehicle': one_vehicle
    }
    return render(request, 'vehicle.html', context)


def rental(request):
    rental = Rental.objects.all()
    context = {
        'rental':rental
    }
    return render(request, 'rent.html', context)

def add_rental(request):
    pass

def rental_id(request, pk):
    pass

