from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signin', views.signin, name='signin'),
    path('student/profile', views.profile, name='profile'),
    path('student/schedule', views.studentSchedule, name='schedule'),
    path('student/tutorsearch', views.tutorsearch, name='tutorsearch'),
    path('tutor/profile', views.tutorProfile, name='tutorProfile'),
    path('tutor/schedule', views.tutorSchedule, name='tutorSchedule'),
]
