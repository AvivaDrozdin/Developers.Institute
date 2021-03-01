from django.db import models


# Create your models here.
class Families(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Animals(models.Model):
    name = models.CharField(max_length=50, default='')
    legs = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    max_speed = models.FloatField(default=0)
    family = models.ForeignKey(Families, on_delete=models.CASCADE)



    
    








