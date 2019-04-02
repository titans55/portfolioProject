from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .hits import insert_hit
from .models import Experience, Education, PlAndTech, Workflow, Interest, About
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
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    plAndTechs = PlAndTech.objects.all()
    workflows = Workflow.objects.all()
    interests = Interest.objects.all()
    abouts = About.objects.all()

    data = {
        'experiences' : experiences,
        'educations' : educations,
        'plAndTechs' : plAndTechs,
        'workflows' : workflows,
        'interests' : interests,
        'abouts' : abouts
    }

    if('isFriend' in request.session):
        if (request.session['isFriend']):
            return render(request, 'welcome.html', {'data' : data})
    return redirect('landingPage')