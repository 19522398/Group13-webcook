from django.db import models

# Create your models here.
class Recipe(models.Model):
    dish_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/recipeimage/', blank=True, null=True)
    ingredients = models.TextField()
    cooking_methods = models.TextField()

def __str__(self):
    return self.dish_name