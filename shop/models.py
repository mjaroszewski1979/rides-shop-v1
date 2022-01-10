from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
    
    def __str__(self):
        return self.title

class Car(models.Model):
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    producer = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500, blank=False)
    country_of_origin = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    production_year = models.CharField(blank=False, max_length=10)
    number_of_doors = models.CharField(blank=False, max_length=10)
    electric = models.BooleanField(blank=False)
    first_owner = models.BooleanField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.producer



