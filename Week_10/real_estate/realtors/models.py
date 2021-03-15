from django.db import models
from datetime import datetime   

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_MVP = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __repr__(self):
        return f'{self.name}'

    #makes realtor visible on browser
    def __str__(self):
        return f'{self.name}'
    