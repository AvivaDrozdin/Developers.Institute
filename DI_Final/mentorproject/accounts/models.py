from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.ForeignKey('ProfileType', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null= True, blank=True)
    location = models.ManyToManyField('Location')
    company = models.CharField(max_length=100, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    skills_have = models.ManyToManyField('Skill', related_name='existing', blank=True)
    skills_wanted = models.ManyToManyField('Skill', related_name='needed', blank=True)
    human_language = models.ManyToManyField('HumanLanguage')

    def __repr__(self):
        return f'{self.user} {self.profile_type}'

    def __str__(self):
        return f'{self.user} {self.profile_type}'


class HumanLanguage(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class ProfileType(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name 