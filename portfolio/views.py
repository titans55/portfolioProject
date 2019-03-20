from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def landingPage(request):

    return render(request, 'landingPage.html')
    
@csrf_exempt
def verifyFriend(request):
    request.session['isFriend'] = True
    return HttpResponse("True")

def welcome(request):

    if('isFriend' in request.session):
        if (request.session['isFriend']):
            return render(request, 'welcome.html')
    return redirect('landingPage')