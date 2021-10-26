from django.urls import include, path
from api import views
#from mysite.api.views import web_json

urlpatterns = [
    path('cars', views.cars_json),
    path('api',views.web_json),
]