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
    path('refresh_database', views.refresh_database),
    path('clear_database', views.clear_database),
    path('update_route', views.update_route),
    path('update_stop', views.update_stop),
]

