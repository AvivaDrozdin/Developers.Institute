from django.db import models


# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country= models.CharField(max_length=100)

    def __repr__(self):
        return f'{self.fname} {self.lname}'
    
    def __str__(self):
        return f'{self.fname} {self.lname}'


class Vehicle_type(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        return f'{self.name}'


class Vehicle_size(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        return f'{self.name}' 


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.SET_NULL, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey(Vehicle_size, on_delete=models.SET_NULL, null = True)

    def __repr__(self):
        return f'{self.vehicle_type}'

    def __str__(self):
        return f'{self.vehicle_type}'



class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f'{self.customer}, {self.vehicle}'
    
    def __str__(self):
        return f'{self.customer}, {self.vehicle}'


class Rental_rate(models.Model):
    daily_rate = models.FloatField(default=0)
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.SET_NULL, null=True)
    vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f'{self.vehicle_type}, {self.Vehicle_size}, self{self.daily_rate}'

    def __str__(self):
        return f'{self.vehicle_type}, {self.Vehicle_size}, self{self.daily_rate}'
