from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import WebcookUser
import json
# Create your views here.

@csrf_exempt

def get_info(request):
    res = None
    user = None
    template = loader.get_template('info.html')
    

    if(request.user.is_authenticated):
        user = request.user
        res = WebcookUser.objects.filter(username=user)
    
    if(request.method == "POST" and request.POST['gender'] and request.POST['age'] and request.POST['weight'] and request.POST['height']):
        if WebcookUser.objects.filter(username=user).count() == 1:
            # Update the existing user information
            WebcookUser.objects.filter(username=user).update(
                age=request.POST['age'],
                weight=request.POST['weight'],
                height=request.POST['height'],
                gender=request.POST['gender']
            )
            
        else:
            # Create a new user entry
            s = WebcookUser(username=user, age=request.POST['age'], weight=request.POST['weight'], height=request.POST['height'], gender=request.POST['gender'])
            s.save()
        res = WebcookUser.objects.filter(username=user)
    print(res)
    context = {
        "user": user,
        "info": res,
    }

    return HttpResponse(template.render(context))
