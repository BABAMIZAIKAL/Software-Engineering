from django.shortcuts import render
from elsys.models import Car
from django.http import response
# Create your views here.
PI = 3.14
import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from api import views
from django.template import loader
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars(request):
    return render(request, 'cars.html')

def board(request):

    data = views.web_json(request)
    text = []
    for word in data['data']:
        d = {}
        d['time'] = word['attributes']['departure_time']
        
        id = word['relationships']['trip']['data']['id']

        for x  in data['included']:
            if word['relationships']['trip']['data']['id'] == x['id']:
                d['destination'] = x['attributes']['headsign']

        if word['relationships']['vehicle']['data'] is None:
            d['train'] = 'None'
        else:
            for y in data['included']:
                if y['id'] == word['relationships']['vehicle']['data']['id']:
                    d['train'] = y['attributes']['label']
        
        
        d['track'] = 'TDB'

        d['status'] = word['attributes']['status']
        text.append(d)
 

    template = loader.get_template('board.html')
    return render(request, 'board.html', {'data':text})

