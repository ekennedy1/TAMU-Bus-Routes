from django.db import models
from django.utils import timezone

# Any time this is updated, run:
    # python manage.py makemigrations Main
    # python manage.py sqlmigrate Main [4-digit number]
    # python manage.py migrate

class Routes(models.Model):
    routeID = models.PositiveIntegerField(primary_key=True)
    routeName = models.TextField()
    routeNumber = models.TextField()
    offCampus = models.BooleanField()
    gameDay = models.BooleanField(default=0)
    date = models.DateField(default=timezone.now)
    def __str__ (self):
        return self.item

class Stops(models.Model):
    stopID = models.PositiveIntegerField(primary_key=True)
    stopName = models.TextField()
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    waypoint = models.BooleanField(default=1)
    longitude = models.FloatField()
    latitude = models.FloatField()
    stopNum = models.PositiveIntegerField()
    def __str__ (self):
        return self.item

class Times(models.Model):
    timeID = models.PositiveIntegerField(primary_key=True)
    stop = models.ForeignKey(Stops, on_delete=models.CASCADE)
    time = models.TimeField()
    def __str__ (self):
        return self.item
