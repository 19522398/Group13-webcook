from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def Logout(request):
    logout(request)
    return redirect('/')