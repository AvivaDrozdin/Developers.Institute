from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+'...' #will display first 150 chr