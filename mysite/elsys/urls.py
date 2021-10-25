from django.urls import include, path
from elsys import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.index),
    path('about', views.about),
    path('cars', views.cars),
]
