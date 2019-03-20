from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def landingPage(request):

    return render(request, 'landingPage.html')

def verifyFriend(request):
    request.session['isFriend'] = True
    return HttpResponse("True")

def welcome(request):

    if('isFriend' in request.session):
        if (request.session['isFriend']):
            return render(request, 'welcome.html')
    return redirect('landingPage')