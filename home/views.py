from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'home/signIn.html')

def welcome(request):
    return render(request, 'home/welcome.html')

def profile(request):
    return render(request, 'home/studentProfile.html')

def studentSchedule(request):
    return render(request, 'home/studentSchedule.html')

def tutorsearch(request):
    return render(request, 'home/tutorSearch.html')

def tutorProfile(request):
    return render(request, 'home/tutorProfile.html')

def tutorSchedule(request):
    return render(request, 'home/baseTutor.html')

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'tutorSearch.html', 
                  { 'mapbox_access_token': 'pk.eyJ1IjoiZXJpY3Nha215c3RlciIsImEiOiJjazhiMXlxZmUwMWN0M2VxZWp2cGIwcGE3In0.LOR2DgUVncLrbVuaPtD5QA'})
