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

	all_routes = []
	for r in Routes.objects.all():
		route_details = {}
		route_details["ID"] = r.routeID
		route_details["Number"] = r.routeNumber
		route_details["Name"] = r.routeName
		route_details["Area"] = r.area
		stops = []
		for s in Stops.objects.filter(route=r):
			stop = {}
			stop["stopID"] = s.stopID
			stop["Number"] = s.stopNum
			stop["Name"] = s.stopName
			stop["Lat"] = s.latitude
			stop["Long"] = s.longitude
			stop["Timed"] = s.timed
			stop["Times"] = s.times.split()
			stops.append(stop)
		route_details["Stops"] = stops
		all_routes.append(route_details)
    
	lat_a = request.GET.get("lat_a", None)
	long_a = request.GET.get("long_a", None)
	lat_b = request.GET.get("lat_b", None)
	long_b = request.GET.get("long_b", None)
	lat_c = request.GET.get("lat_c", None)
	long_c = request.GET.get("long_c", None)
	lat_d = request.GET.get("lat_d", None)
	long_d = request.GET.get("long_d", None)
	lat_e = request.GET.get("lat_e", None)
	long_e = request.GET.get("long_e", None)
	lat_f = request.GET.get("lat_f", None)
	long_f = request.GET.get("long_f", None)
	lat_g = request.GET.get("lat_g", None)
	long_g = request.GET.get("long_g", None)
	lat_h = request.GET.get("lat_h", None)
	long_h = request.GET.get("long_h", None)
	lat_i = request.GET.get("lat_i", None)
	long_i = request.GET.get("long_i", None)
	lat_j = request.GET.get("lat_j", None)
	long_j = request.GET.get("long_j", None)
	lat_k = request.GET.get("lat_k", None)
	long_k = request.GET.get("long_k", None)
	lat_l = request.GET.get("lat_l", None)
	long_l = request.GET.get("long_l", None)
	lat_m = request.GET.get("lat_m", None)
	long_m = request.GET.get("long_m", None)
	lat_n = request.GET.get("lat_n", None)
	long_n = request.GET.get("long_n", None)
	lat_o = request.GET.get("lat_o", None)
	long_o = request.GET.get("long_o", None)
	lat_p = request.GET.get("lat_p", None)
	long_p = request.GET.get("long_p", None)
	lat_q = request.GET.get("lat_q", None)
	long_q = request.GET.get("long_q", None)
	lat_r = request.GET.get("lat_r", None)
	long_r = request.GET.get("long_r", None)
	lat_s = request.GET.get("lat_s", None)
	long_s = request.GET.get("long_s", None)
	lat_t = request.GET.get("lat_t", None)
	long_t = request.GET.get("long_t", None)
	lat_u = request.GET.get("lat_u", None)
	long_u = request.GET.get("long_u", None)
	lat_v = request.GET.get("lat_v", None)
	long_v = request.GET.get("long_v", None)
	lat_w = request.GET.get("lat_w", None)
	long_w = request.GET.get("long_w", None)

	if lat_a and lat_b and lat_c and lat_d and lat_e and lat_f and lat_g and lat_h and lat_i and lat_j and lat_k and lat_l and lat_m and lat_n and lat_o and lat_p and lat_q and lat_r and lat_s and lat_t and lat_u and lat_v and lat_w:
		directions = Directions(
			lat_a= lat_a,
			long_a=long_a,
			lat_b = lat_b,
			long_b=long_b,
			lat_c= lat_c,
			long_c=long_c,
			lat_d = lat_d,
			long_d =long_d,
			lat_e = lat_e,
			long_e = long_e,
			lat_f = lat_f,
			long_f= long_f,
			lat_g = lat_g,
			long_g= long_g,
			lat_h = lat_h,
			long_h= long_h,
			lat_i = lat_i,
			long_i=long_i,
			lat_j= lat_j,
			long_j=long_j,
			lat_k = lat_k,
			long_k =long_k,
			lat_l = lat_l,
			long_l = long_l,
			lat_m = lat_m,
			long_m= long_m,
			lat_n = lat_n,
			long_n= long_n,
			lat_o = lat_o,
			long_o= long_o,
			lat_p = lat_p,
			long_p= long_p,
			lat_q = lat_q,
			long_q=long_q,
			lat_r= lat_r,
			long_r=long_r,
			lat_s = lat_s,
			long_s =long_s,
			lat_t = lat_t,
			long_t = long_t,
			lat_u = lat_u,
			long_u= long_u,
			lat_v = lat_v,
			long_v= long_v,
			lat_w = lat_w,
			long_w= long_w
			)
	else:
		return redirect(reverse('main:route'))

	context = {
		"MAP_KEY": settings.MAP_KEY,
		"base_country": settings.BASE_COUNTRY,
		"ALL_ROUTES": all_routes,
		"lat_a": lat_a,
		"long_a": long_a,
		"lat_b": lat_b,
		"long_b": long_b,
		"lat_c": lat_c,
		"long_c": long_c,
		"lat_d": lat_d,
		"long_d": long_d,
		"lat_e": lat_e,
		"long_e": long_e,
		"lat_f": lat_f,
		"long_f": long_f,
		"lat_g": lat_g,
		"long_g": long_g,
		"lat_h": lat_h,
		"long_h": long_h,
		"lat_i": lat_i,
		"long_i": long_i,
		"lat_j": lat_j,
		"long_j": long_j,
		"lat_k": lat_k,
		"long_k": long_k,
		"lat_l": lat_l,
		"long_l": long_l,
		"lat_m": lat_m,
		"long_m": long_m,
		"lat_n": lat_n,
		"long_n": long_n,
		"lat_o": lat_o,
		"long_o": long_o,
		"lat_p": lat_p,
		"long_p": long_p,
		"lat_q": lat_q,
		"long_q": long_q,
		"lat_r": lat_r,
		"long_r": long_r,
		"lat_s": lat_s,
		"long_s": long_s,
		"lat_t": lat_t,
		"long_t": long_t,
		"lat_u": lat_u,
		"long_u": long_u,
		"lat_v": lat_v,
		"long_v": long_v,
		"lat_w": lat_w,
		"long_w": long_w,
		"origin": f'{lat_a}, {long_a}',
		"destination": f'{lat_b}, {long_b}',
		"directions": directions,
	}
	return render(request, 'main/map.html', context)

def route(request):

	all_routes = []
	for r in Routes.objects.all():
		route_details = {}
		route_details["ID"] = r.routeID
		route_details["Number"] = r.routeNumber
		route_details["Name"] = r.routeName
		route_details["Area"] = r.area
		stops = []
		for s in Stops.objects.filter(route=r):
			stop = {}
			stop["stopID"] = s.stopID
			stop["Number"] = s.stopNum
			stop["Name"] = s.stopName
			stop["Lat"] = s.latitude
			stop["Long"] = s.longitude
			stop["Timed"] = s.timed
			stop["Times"] = s.times.split()
			stops.append(stop)
		route_details["Stops"] = stops
		all_routes.append(route_details)

	routeName = request.session["routeName"]
	routeNumber = request.session["routeNumber"]
	sourceStop = request.session["sourceStop"]
	destStop = request.session["destStop"]
    
	context = {
		"MAP_KEY": settings.MAP_KEY,
		"MAP_URL": "https://maps.googleapis.com/maps/api/js?key=" + settings.MAP_KEY + "&callback=initMap",
		"base_country": settings.BASE_COUNTRY,
		"ALL_ROUTES": all_routes,
		"ROUTE_NAME": routeName,
		"ROUTE_NUMBER": routeNumber,
		"SOURCE_STOP": sourceStop,
		"DEST_STOP": destStop,
	}
	return render(request, 'main/route.html', context)

def update_stop(request):
	print("Updating stop")
	request.session["routeName"] = request.GET.get('routeName', None)
	request.session["routeNumber"] = request.GET.get('routeNumber', None)
	request.session["sourceStop"] = request.GET.get('sourceStop', None)
	request.session["destStop"] = request.GET.get('destStop', None)
	print(request.session["routeName"])
	return redirect('/home')

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
				stopDesc = "This is where the description would go if it were manually added to the database.",
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
	all_routes = []
	for r in Routes.objects.all():
		all_details = {}
		all_details["Name"] = r.routeName
		all_details["Number"] = r.routeNumber
		all_details["ID"] = r.routeID
		all_routes.append(all_details)
	routes_display = []
	if not request.session.has_key("tableDisplay"):
		request.session["tableDisplay"] = "All"
	if request.session["tableDisplay"] == "All":
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
			routes_display.append(route_details)
	elif request.session["tableDisplay"] == "On":
		for r in Routes.objects.filter(area="On Campus"):
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
			routes_display.append(route_details)
	elif request.session["tableDisplay"] == "Off":
		for r in Routes.objects.filter(area="Off Campus"):
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
			routes_display.append(route_details)
	else:
		for r in Routes.objects.filter(routeID=request.session["tableDisplay"]):
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
			routes_display.append(route_details)
	context = {
		"ALL_ROUTES": all_routes,
		"ROUTES_DISPLAY": routes_display,
	}
	return render(request, 'main/stops.html', context)

def update_route(request):
	request.session["tableDisplay"] = request.GET.get('selectedID', None)
	return redirect('/routes')

def twitter(request):
    return render(request, 'main/twitter.html')