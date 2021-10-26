from django.urls import include, path
from elsys import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('cars', views.cars),
    path('board',views.board),
    path('', views.board),
]