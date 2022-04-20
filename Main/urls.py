from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.route, name="route"),
    path('map', views.map, name="map"),
    path('schedule', views.schedule),
    path('routes', views.stops),
    path('updates', views.twitter),
]

