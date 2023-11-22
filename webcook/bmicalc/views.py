from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def BMI(request):
    template = loader.get_template('bmi.html')

    bmi = None
    message = None
    if(request.method == "POST" and request.POST['height'] and request.POST['weight'] and request.POST['age']):
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        age = int(request.POST['age'])
        bmi = weight / (height*height)

        if(age < 18):
            context = {
                'message': "Sorry, you must be older than 18 years old to do BMI calculate"
            }
            return HttpResponse(template.render(context))
    
        else:
            if(bmi < 18.5):
                context = {
                    'result': bmi,
                    'message': "It's seems like you are underweight, but don't worry, these articles provided down there can help you gain some weight" 
                }
                return HttpResponse(template.render(context))
            elif (bmi >= 18.5 and bmi <= 24.9):
                context = {
                    'result': bmi,
                    'message': "Your BMI indicates you are healthy, good job, keep up the work"
                }   
                return HttpResponse(template.render(context))
            elif(bmi >= 25 and bmi <= 29.9):
                context = {
                    'result': bmi,
                    'message': "It's seems you are a bit overweight, losing some maybe the best idea, these articles provided down there can help you lose some weight"
                }
                return HttpResponse(template.render(context))
            else:
                context = {
                   'result': bmi,
                    'message': "You are, quite over the chart, these articles provided down there can help you lose some weight"
                }
                return HttpResponse(template.render(context))
    context = {
        'result':bmi,
        'message': message
    }
    return HttpResponse(template.render(context))
