from django.shortcuts import render

# Create your views here.

from elsys.models import Car
from api.serializers import CarSerializer
from django.http import JsonResponse

def cars_json(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return JsonResponse({'data': serializer.data }, safe=False)