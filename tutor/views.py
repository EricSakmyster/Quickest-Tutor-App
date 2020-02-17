from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Tutor App!")

def signup(request):
    return HttpResponse("Welcome to the Signup Page")

def profile(request):
    return HttpResponse("Student Tab Profile")

def schedule(request):
    return HttpResponse("Student Tab Schedule")

