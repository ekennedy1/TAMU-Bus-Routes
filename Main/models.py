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
    area = models.TextField()
    # gameDay = models.BooleanField(default=0) # (would include w/ more dates)
    # date = models.DateField(default=timezone.now) # (would include w/ more dates)
    def __str__ (self):
        return self.item

class Stops(models.Model):
    stopID = models.PositiveIntegerField(primary_key=True)
    stopName = models.TextField()
    stopDesc = models.TextField()
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    # waypoint = models.BooleanField(default=1) # (would include w/ bus location tracking)
    longitude = models.FloatField() # still need to fix
    latitude = models.FloatField() # still need to fix
    stopNum = models.PositiveIntegerField()
    timed = models.BooleanField(default=0)
    def __str__ (self):
        return self.item

class Times(models.Model):
    timeID = models.PositiveIntegerField(primary_key=True)
    stop = models.ForeignKey(Stops, on_delete=models.CASCADE)
    time = models.TimeField()
    def __str__ (self):
        return self.item
