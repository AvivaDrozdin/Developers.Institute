from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    image = models.URLField(max_length=500, null=True)
    points = models.IntegerField(max_length=500, default=0)


    def __repr__(self):
        return f'{self.username}'

    def __str__(self):
        return f'{self.username}'

