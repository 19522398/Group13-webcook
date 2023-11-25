from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import WebcookUser
# Create your views here.

@csrf_exempt

def get_info(request):
    res = None
    user = None
    template = loader.get_template('info.html')
    if(request.user.is_authenticated):
        user = request.user
        res = WebcookUser.objects.filter(name=user)

    if(request.method == "POST" and request.POST['age'] and request.POST['weight'] and request.POST['height'] and WebcookUser.objects.filter(name=user).count() == 0):
        s = WebcookUser(name=user,age=request.POST['age'], weight=request.POST['weight'],height=request.POST['height'])
        s.save()
        
        res = WebcookUser.objects.filter(name=user)
        print(res.values())
    context = {
        "user": user,
        "info": res
    }
    return HttpResponse(template.render(context))
