from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Hit
import datetime

# Using this library
# https://pypi.org/project/django-user_agents/


def insert_hit(request, page_name):


    endPoint = request.build_absolute_uri()
    ip = get_client_ip(request)

    country = getUserCountry(ip)

    referer = request.META.get('HTTP_REFERER')

    browser_family = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    browser = browser_family + ' ' + browser_version

    os_family = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    os = os_family + ' ' + os_version

    device = request.user_agent.device.family
    
        
    now = datetime.datetime.now()

    # Features of the device
    mobile = request.user_agent.is_mobile
    tablet = request.user_agent.is_tablet
    touch = request.user_agent.is_touch_capable
    pc = request.user_agent.is_pc
    bot = request.user_agent.is_bot
    

    Hit.objects.create(page_name = page_name,
                       endpoint = endPoint,
                       country = country,
                       device_ip = ip,
                       browser = browser,
                       os = os,
                       referer = referer,
                       time = now,
                       device = device,
                       mobile = mobile,
                       tablet = tablet,
                       touch = touch,
                       pc = pc,
                       bot = bot)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from  urllib.request import urlopen, Request
import re, socket
from django.conf import settings


def getUserCountry(ip):
    url = "http://api.wipmania.com/" + ip 
    socket.setdefaulttimeout(5)
    headers = {'Typ':'django','Ver':'1.1.1','Connection':'Close'}
    try:
        req = Request(url, None, headers)
        urlfile = urlopen(req)
        land = urlfile.read()
        urlfile.close()
        return land[:2]
    except Exception:
        return "XX"
