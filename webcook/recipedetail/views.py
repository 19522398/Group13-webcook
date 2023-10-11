#from django.shortcuts import render

# Create your views here.
from .models import Recipe
from django.views.generic import TemplateView
from django.db.models import Q
from search.models import Recipe

class Details(TemplateView):
    model = Recipe
    template_name = 'recipe.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(Q(dish_name__icontains=query) | Q(ingredients__icontains=query))
        return object_list
    


