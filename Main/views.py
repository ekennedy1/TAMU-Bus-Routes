from django.shortcuts import render, redirect, reverse
from django.conf import settings
from Main.mixins import Directions
import requests
from .models import Routes, Stops
from django.http import HttpResponse
from pyproj import Transformer


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

def clear_database(request):
	# delete all database data
	Routes.objects.all().delete()
	Stops.objects.all().delete()
	# return HTTPResponse
	print("Deleted all routes, stops, and times.")
	return HttpResponse({}, content_type="application/json")

def refresh_database(request):
	# delete all database data
	Routes.objects.all().delete()
	Stops.objects.all().delete()
	# data = get data from the api
	routes_json = requests.get('https://transport.tamu.edu/BusRoutesFeed/api/Routes').json()
	# data [1, 2]
	# stop_data = []
	routes_list = []
	route_id = 1
	# for x in data:
	for i in routes_json:
		# creating all objects as a list:
	    # stop_data.append(Stops(
	        # stopName=x["stopName"],
	    # ))
		routes_list.append(Routes(
			routeID = route_id,
			routeName = i.get('Name'),
			routeNumber = i.get('ShortName'),
			area = i.get('Group').get('Name')
		))
		route_id = route_id + 1
		# what creating a single object would be like:
		# Stops.objects.create(
		    # stopName=x["stopName"],
		# )
	# Stops.objects.bulk_create(stop_data)
	Routes.objects.bulk_create(routes_list)

	stops_list = []
	stop_id = 1
	for r in Routes.objects.all():
		stops_json = requests.get('https://transport.tamu.edu/BusRoutesFeed/api/route/' + r.routeNumber + '/stops').json()
		times_json = requests.get('https://transport.tamu.edu/BusRoutesFeed/api/Route/' + r.routeNumber + '/TimeTable').json()
		stop_num = 1
		time_stop_num = 1
		for i in stops_json:
			times_text = ""
			times_list = []
			for j in times_json:
				time_num = 1
				for key in j:
					if time_num == time_stop_num:
						if j[key] != None:
							# time calculation from "HH:MM AM/PM" to "HH:MM" (24-hour)
							if j[key][-2:] == "AM":
								times_list.append(j[key][:5])
							elif j[key][-2:] == "PM":
								if j[key][:2] == "12":
									times_list.append(j[key][:5])
								else:
									times_list.append(str(int(j[key][:2]) + 12) + j[key][2:5])
					time_num = time_num + 1
			for t in times_list:
				if times_text == "":
					times_text = t
				else:
					times_text = times_text + " " + t
			transformer = Transformer.from_crs("epsg:102100","epsg:4326")
			coords = transformer.transform(i.get('Longtitude'), i.get('Latitude'))
			stops_list.append(Stops(
				stopID = stop_id,
				stopNum = stop_num,
				stopName = i.get('Name'),
				stopDesc = "This is where the description will go once it is manually added to the database.",
				route = r,
				longitude = coords[1],
				latitude = coords[0],
				timed = i.get('Stop').get('IsTimePoint'),
				times = times_text
			))
			stop_id = stop_id + 1
			stop_num = stop_num + 1
			if i.get('Stop').get('IsTimePoint'):
				time_stop_num = time_stop_num + 1
	Stops.objects.bulk_create(stops_list)

	# return HTTPResponse
	print("Recreated all routes, stops, and times.")
	return HttpResponse({}, content_type="application/json")

def stops(request):
	routes_list = []
	for r in Routes.objects.all():
		route_details = {}
		route_details["Number"] = r.routeNumber
		route_details["Name"] = r.routeName
		route_details["Area"] = r.area
		stops = []
		for s in Stops.objects.filter(route=r):
			stop = {}
			stop["Number"] = s.stopNum
			stop["Name"] = s.stopName
			stop["Desc"] = s.stopDesc
			stop["Long"] = s.longitude
			stop["Lat"] = s.latitude
			stop["Timed"] = s.timed
			times = s.times
			time_list_temp = times.split()
			times = ""
			for x in time_list_temp:
				if times == "":
					times = x
				else:
					times = times + ", " + x
			stop["Times"] = times
			stops.append(stop)
		route_details["Stops"] = stops
		routes_list.append(route_details)
	context = {
		"ROUTE_LIST": routes_list,
	}
	return render(request, 'main/stops.html', context)

def twitter(request):
    return render(request, 'main/twitter.html')