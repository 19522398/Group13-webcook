from typing import Any
#from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from .models import Recipe
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
import re
from django.template import loader
from django.shortcuts import render
# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  context = {}
  if(request.user.is_authenticated):
        context = {
            'user': request.user
        }
        return render(request, 'index.html',context)
  return HttpResponse(template.render(context))

class HomePage(TemplateView):
    template_name = 'index.html'

class SearchResult(ListView):
    model = Recipe
    template_name = 'result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        
        regex = re.compile("[@_!#$%^&*()<>?/\\|}{~:]")   
        check = regex.search(query)
        
        if (query.isdigit() == False and check == None):
            t = query.split(",")
            search = []
        
            for i in t:
                if(i[0].count(" ")): 
                    i = "".join(i.split())
                search.append(i)

            if(len(search) == 1):
                object_list = Recipe.objects.filter(Q(dish_name__icontains=search[0]) | Q(ingredients__icontains=search[0]))
                
            else:
                object_list = Recipe.objects.filter(ingredients__in=search)
                query = Q()
                for ingredient in search:
                    query &= Q(ingredients__icontains=ingredient)

                object_list = Recipe.objects.filter(query)
            
            if(object_list):
                return object_list
        
class NotFound(TemplateView):
    template_name='404.html'

class RecipeDetails(ListView):
    model = Recipe
    template_name = 'recipe.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(Q(dish_name__icontains=query))
        return object_list
