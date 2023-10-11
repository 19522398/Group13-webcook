from django.contrib import admin
from .models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["dish_name", "image", "ingredients", "cooking_methods"]

admin.site.register(Recipe, RecipeAdmin)

