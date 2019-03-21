from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .hits import insert_hit

# Create your views here.

def landingPage(request):
    insert_hit(request, 'landingPage')
    return render(request, 'landingPage.html')
    
@csrf_exempt
def verifyFriend(request):
    insert_hit(request, 'verifyFriend')

    request.session['isFriend'] = True
    return HttpResponse("True")

def welcome(request):
    insert_hit(request, 'welcome')

    if('isFriend' in request.session):
        if (request.session['isFriend']):
            return render(request, 'welcome.html')
    return redirect('landingPage')