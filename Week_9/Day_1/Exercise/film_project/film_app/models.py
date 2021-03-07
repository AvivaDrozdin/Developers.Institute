from django.db import models
from django.utils.timezone import now


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField(default=now, editable=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='films_created')
    available_in_countries = models.ManyToManyField(Country, related_name='films_available')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

    def __repr__(self):
        return f'{self.title}, {self.release_date}'

    def __str__(self):
        return f'{self.title}, {self.release_date}'


