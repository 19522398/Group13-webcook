from django.db import models
from django.contrib import admin
# Create your models here.

class WebcookUser(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(null=True)
    weight = models.CharField(max_length=4)
    height = models.CharField(max_length=3)
    age = models.CharField(max_length=3)

admin.site.register(WebcookUser)