from django.shortcuts import render, redirect, reverse
from django.conf import settings

from Main.mixins import Directions


def home(request):
    context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
    return render(request, 'mapHome.html', context)

def stops(request):

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
	    return redirect(reverse('Main:home'))

    context = {
	"google_api_key": settings.GOOGLE_API_KEY,
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
    return render(request, 'stops.html', context)

def schedule(request):
    return render(request, 'schedule.html')

def twitter(request):
    return render(request, 'twitter.html')