from django import forms
from .models import *

class Add_customer(forms.Form):
    fname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country= models.CharField(max_length=100)

class Add_rental(forms.Form):
    customer = forms.IntegerField()
    vehicle = forms.IntegerField()


class Add_vehicle(forms.Form):
    Vehicle_type = forms.IntegerField(widget=forms.Select())
    size = forms.IntegerField(widget=forms.Select())
    
