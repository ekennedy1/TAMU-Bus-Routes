from django.core.management.base import BaseCommand, CommandError
from Main.models import Routes, Stops
from pyproj import Transformer
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
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
