from django.http import HttpResponse
from django.shortcuts import render
import requests

from .models import Car


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    response = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Cvehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north').json()
    data = []
    for j in response['data']:
        entry = {}
        entry['time'] = j['attributes']['departure_time']



        if j['relationships']['trip']['data'] is None:
            entry['destination'] = "None"
        else:
            destination = requests.get('https://api-v3.mbta.com/trips?filter[id]=' + j['relationships']['trip']['data']['id']).json()
            entry['destination'] = destination['data'][0]['attributes']['headsign']

        if j['relationships']['vehicle']['data'] is None:
            entry['vehicle'] = "None"
        else:
            vehicle = requests.get('https://api-v3.mbta.com/vehicles?filter[id]=' + j['relationships']['vehicle']['data']['id']).json()
            entry['vehicle'] = vehicle['data'][0]['attributes']['label']

        entry['track'] = "TBD"

        entry['status'] = j['attributes']['status']


        data.append(entry)

    data.reverse()
    return render(request, "home.html", {'response':data})

def about(request):
    return render(request, "home.html")

def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})
