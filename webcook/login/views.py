from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages 
import random
from django.contrib.auth.hashers import make_password

# Create your views here.

@csrf_exempt
def Login(request):
    if(request.method=='POST'):
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username=username, password=passw)

        if user is not None:
            login(request,user)
            context = {
            'user': request.user
            }
            return redirect('/')
        else :
            messages.error(request,"Username or password is incorrect")

    return render(request, 'login.html')