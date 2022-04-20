from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home),
    path('map', views.home),
    path('home', views.home),
    path('routes', views.stops),
    path('calendar', views.schedule),
    path('updates', views.twitter),
]

