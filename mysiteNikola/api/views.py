from typing import Text
from django.shortcuts import render
from elsys.models import Car
from api.serializers import CarSerializer
from django.http import JsonResponse
import requests

from api import views
from django.template import loader

def cars_json(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return JsonResponse({'data': serializer.data }, safe=False)

def web_json(request): 
    return requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=vehicle%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north', headers={'Content-type': 'application/json'}).json()
