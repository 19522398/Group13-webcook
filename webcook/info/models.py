from django.db import models

# Create your models here.

class WebcookUser(models.Model):
    name = models.CharField(max_length=100)
    weight = models.CharField(max_length=4)
    height = models.CharField(max_length=3)
    age = models.CharField(max_length=3)
