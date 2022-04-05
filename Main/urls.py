from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home),
    path('map', views.home),
    path('home', views.home),
    path('stops', views.stops),
    path('schedule', views.schedule),
    path('twitter', views.twitter),
]
