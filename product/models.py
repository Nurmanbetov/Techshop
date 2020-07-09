from django.db import models
from django.contrib.auth.models import User 


class Product(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    price = models.IntegerField()
    sold = models.IntegerField(default=0)
    active = models.IntegerField(default=True)
    
