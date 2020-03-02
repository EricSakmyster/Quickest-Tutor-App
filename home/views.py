from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'home/signIn.html')

def profile(request):
    return render(request, 'home/studentProfile.html')

def studentSchedule(request):
    return render(request, 'home/studentSchedule.html')

def tutorsearch(request):
    return render(request, 'home/tutorSearch.html')

def tutorProfile(request):
    return HttpResponse(request, 'home/tutorProfile.html')

def tutorSchedule(request):
    return render(request, 'home/baseTutor.html')


