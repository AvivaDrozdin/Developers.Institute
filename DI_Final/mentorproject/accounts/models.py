from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('HEB', 'עברית'),
    ('ARA', 'العربية'),
    ('RUS', 'Русский'),
    ('ESP', 'Spanish'),
    ('FRE', 'Français'),
    ]
    DISTRICT_CHOICES = [
    ('online', 'Online'),
    ('tlv', 'Tel Aviv District'),
    ('central', 'Central District'),
    ('jerusalem', 'Jerusalem District'),
    ('haifa', 'Haifa District'),
    ('north', 'Northern District'),
    ('south', 'Southern District'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.ForeignKey('ProfileType', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    location = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    company = models.CharField(max_length=100, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    skills_have = models.ManyToManyField('Skill', related_name='existing')
    skills_wanted = models.ManyToManyField('Skill', related_name='needed')
    human_language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default='English')




class Skill(models.Model):
    name = models.CharField(max_length=100)


# make language model


class ProfileType(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name 