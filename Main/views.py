from django.shortcuts import render, redirect, reverse
from django.conf import settings
from Main.mixins import Directions
import requests
from . import models


def home(request):

	context = {
		"MAP_KEY": settings.MAP_KEY,
		"MAP_URL": "https://maps.googleapis.com/maps/api/js?key=" + settings.MAP_KEY + "&callback=initMap",
		"base_country": settings.BASE_COUNTRY
	}
	return render(request, 'main/mapHome.html', context)

def map(request):
    
	lat_a = request.GET.get("lat_a", None)
	long_a = request.GET.get("long_a", None)
	lat_b = request.GET.get("lat_b", None)
	long_b = request.GET.get("long_b", None)
	lat_c = request.GET.get("lat_c", None)
	long_c = request.GET.get("long_c", None)
	lat_d = request.GET.get("lat_d", None)
	long_d = request.GET.get("long_d", None)

	if lat_a and lat_b and lat_c and lat_d:
		directions = Directions(
			lat_a= lat_a,
			long_a=long_a,
			lat_b = lat_b,
			long_b=long_b,
			lat_c= lat_c,
			long_c=long_c,
			lat_d = lat_d,
			long_d=long_d
			)
	else:
		return redirect(reverse('main:route'))

	context = {
		"MAP_KEY": settings.MAP_KEY,
		"base_country": settings.BASE_COUNTRY,
		"lat_a": lat_a,
		"long_a": long_a,
		"lat_b": lat_b,
		"long_b": long_b,
		"lat_c": lat_c,
		"long_c": long_c,
		"lat_d": lat_d,
		"long_d": long_d,
		"origin": f'{lat_a}, {long_a}',
		"destination": f'{lat_b}, {long_b}',
		"directions": directions,
	}
	return render(request, 'main/map.html', context)

def route(request):
    
	context = {
		"MAP_KEY": settings.MAP_KEY,
		"MAP_URL": "https://maps.googleapis.com/maps/api/js?key=" + settings.MAP_KEY + "&callback=initMap",
		"base_country": settings.BASE_COUNTRY,
	}
	return render(request, 'main/route.html', context)

def calendar(request):
	return render(request, 'main/schedule.html')

def stops(request):
	routes_json = requests.get('https://transport.tamu.edu/BusRoutesFeed/api/Routes').json()
	routes_list = []
	for i in routes_json:
		route_details = {}
		route_details["Number"] = i.get('ShortName')
		route_details["Name"] = i.get('Name')
		stops = []
		stops_json = requests.get('https://transport.tamu.edu/BusRoutesFeed/api/route/' + route_details["Number"] + '/stops').json()
		for j in stops_json:
			stop = {}
			stop["Name"] = j.get('Name')
			stop["Rank"] = j.get('Rank')
			stop["Long"] = j.get('Longtitude')
			stop["Lat"] = j.get('Latitude')
			stop["Timed"] = j.get('IsTimePoint')
			stops.append(stop)
		route_details["Stops"] = stops
		routes_list.append(route_details)
	context = {
		"TEST_DICT": requests.get('https://transport.tamu.edu/BusRoutesFeed/api/route/12/stops').json(),
		"TEST_KEY": requests.get('https://transport.tamu.edu/BusRoutesFeed/api/route/12/stops').json()[0].get('Key'),
		"ALL_ROUTES": requests.get('https://transport.tamu.edu/BusRoutesFeed/api/Routes').json(),
		"ROUTE_LIST": routes_list,
	}
	return render(request, 'main/stops.html', context)

def twitter(request):
    return render(request, 'main/twitter.html')