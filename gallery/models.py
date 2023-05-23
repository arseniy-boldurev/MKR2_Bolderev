from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    categories = models.ManyToManyField(Category, blank=True)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()
