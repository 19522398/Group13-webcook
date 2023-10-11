from typing import Any
#from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from .models import Recipe
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
import re
# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

class SearchResult(ListView):
    model = Recipe
    template_name = 'result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
        check = regex.search(query)
        if (query.isdigit() == False and check == 0):
            object_list = Recipe.objects.filter(Q(dish_name__icontains=query) | Q(ingredients__icontains=query))
            if(object_list):
                return object_list
        else:
            raise Http404("Query not legit, it's should be words, not number or any special characters")
        
class NotFound(TemplateView):
    template_name='404.html'

class RecipeDetails(ListView):
    model = Recipe
    template_name = 'recipe.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(Q(dish_name__icontains=query))
        return object_list

