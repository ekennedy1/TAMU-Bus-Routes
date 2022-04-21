from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.route, name="route"),
    path('home', views.route, name="route"),
    path('map', views.map, name="map"),
    path('calendar', views.calendar),
    path('routes', views.stops),
    path('updates', views.twitter),
]

