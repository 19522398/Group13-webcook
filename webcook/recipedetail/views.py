from django.shortcuts import render
from typing import Any
#from django.db.models.query import QuerySet
from django.db.models import Q
from django.http import HttpResponse
import re
from django.template import loader
import requests
from search.models import Recipe
import comment.views
from comment.models import Comment
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

model = Recipe
template = loader.get_template('recipe.html')

@csrf_exempt
def get_queryset(request):
    template = loader.get_template('recipe.html')
    user = request.user
    query = request.GET.get("q")
    object_list = Recipe.objects.filter(Q(dish_name__icontains=query))
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'QIYWhfjMhNHSe3coceHJGA==WlJx0O4NcxmPSjW6','Origin':'api.calorieninjas.com'})
    res = response.json()
    comm = None
    if(comment.views.comment_list(request)):
        comm = Comment.objects.filter(Q(dish_name__icontains=query))
    print(res)
    context = {
        "object_list": object_list,
        "res": res,
        "user":user,
        "comments":comm,
    }
    return HttpResponse(template.render(context))