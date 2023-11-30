from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse, parse_qs


# Create your views here.
@csrf_exempt
def comment_list(request):
    
    parsed_url = urlparse(request.META.get('HTTP_REFERER', '/'))
    query_params = parse_qs(parsed_url.query)
    dn = query_params.get('q', [''])[0]

    print(request.POST)

    if (request.method == 'POST' and request.POST['comment']):
        user = "AnonymousUser"
        
        if request.user.is_authenticated:
            user = request.user

        comment = Comment(name=user,content=request.POST.get('comment'),dish_name=dn)
        comment.save()

    
    return redirect(request.META.get('HTTP_REFERER', '/'))