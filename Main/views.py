from django.shortcuts import render

def home(request):
    return render(request, 'mapHome.html')

def stops(request):
    return render(request, 'stops.html')

def schedule(request):
    return render(request, 'schedule.html')

def twitter(request):
    return render(request, 'twitter.html')