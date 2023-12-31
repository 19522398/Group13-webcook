# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calories(request):
    res = None
    user = None
    if(request.user.is_authenticated):
        user = request.user
    template = loader.get_template('calories.html')
    if(request.method =='POST' and request.POST['calories']):
        data = request.POST['calories']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        query = data
        response = requests.get(api_url + query, headers={'X-Api-Key': 'QIYWhfjMhNHSe3coceHJGA==WlJx0O4NcxmPSjW6','Origin':'api.calorieninjas.com'})
        res = response.json()
    context = {
    'res':res,
    'user':user
    }
    return HttpResponse(template.render(context))
