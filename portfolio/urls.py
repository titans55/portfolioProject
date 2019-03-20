from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('welcome', views.welcome, name='welcome'),
    #AJAX
    path('verifyFriend', views.verifyFriend, name='verifyFriend')
]