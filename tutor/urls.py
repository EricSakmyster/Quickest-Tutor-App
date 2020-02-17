from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('student/profile', views.profile, name='profile'),
    path('student/schedule', views.schedule, name='schedule'),
    path('student/tutorsearch', views.tutorsearch, name='tutorsearch'),
    path('tutor/profile', views.tutorProfile, name='tutorProfile'),
    path('tutor/schedule', views.tutorSchedule, name='tutorSchedule'),
]
