from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('signin', views.signin, name='signin'),
    path('studentProfile', views.profile, name='profile'),
    path('editSP', views.editSP, name='editSP'),
    path('studentSchedule', views.index, name='schedule'),
    path('studentTutorSearch', views.tutorsearch, name='tutorsearch'),
    path('tutorProfile', views.tutorProfile, name='tutorProfile'),
    path('editTP', views.editTP, name='editTP'),
    path('tutorSchedule', views.tutorSchedule, name='tutorSchedule'),
]
