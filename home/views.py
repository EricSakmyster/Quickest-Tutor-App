from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Tutor App!")

def signup(request):
    return render(request, 'home/index.html')

def profile(request):
    return render(request, 'home/studentProfile.html')

def studentSchedule(request):
    return render(request, 'home/studentSchedule.html')

def tutorsearch(request):
    return render(request, 'home/tutorSearch.html')

def tutorProfile(request):
    return HttpResponse("Tutor Tab Profile")

def tutorSchedule(request):
    return render(request, 'home/baseTutor.html')


