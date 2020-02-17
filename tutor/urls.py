from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/profile', views.profile, name='profile'),
    path('student/schedule', views.schedule, name='schedule'),
    path('student/tutorsearch', views.tutorsearch, name='tutorsearch'),
]
