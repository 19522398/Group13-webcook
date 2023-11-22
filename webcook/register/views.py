from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages 
import random
from django.contrib.auth.hashers import make_password

# Create your views here.
def checknum (s):
    for i in s:
        if(i.isdigit()):
            return True
    return False


@csrf_exempt
def Register(request):
    template = loader.get_template('register.html')
    name = None
    if(request.method=='POST' and request.POST['pass'] and request.POST['email']) and request.POST['pass2'] and request.POST['user']:
        
        username = request.POST['user']
        passw = request.POST['pass']
        passw2 = request.POST['pass2']
        mail = request.POST["email"]

        print(username, passw, passw2, mail)

        if User.objects.filter(username=username):
            context = {
            'email': mail,
            'username': username,
            'message': 'The username already exists !!'
            }
            return HttpResponse(template.render(context))
        
        if User.objects.filter(email=mail):
            context = {
            'email': mail,
            'username': username,
            'message': 'The email already exists !!'
            }
            return HttpResponse(template.render(context))
        if len(passw) < 8 or checknum(passw) == 0:
            context = {
            'email': mail,
            'message': 'Password must container at least 8 characters and 1 number.'
            }
            return HttpResponse(template.render(context))
        if passw != passw2:
            context = {
            'email': mail,
            'message': "Password didn't match."
            }
            return HttpResponse(template.render(context))

        myuser = User.objects.create_user(username ,mail, passw)
        messages.success(request,"Your account had been created")
        myuser.save()
        return redirect('login')
    
    context = {
    'username':name
    }
    return HttpResponse(template.render(context))

