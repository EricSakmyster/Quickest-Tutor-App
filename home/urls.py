from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    path('welcome', views.WelcomeView.as_view(), name='welcome'),
    path('signin', views.signin, name='signin'),
    path('studentProfile', views.profile, name='profile'),
    path('editSP', views.editSP, name='editSP'),
    path('studentSchedule', views.index, name='schedule'),
    path('studentTutorSearch', views.tutorsearch, name='tutorsearch'),
    path('tutorProfile', views.tutorProfile.as_view(), name='tutorProfile'),
    path('editTP', views.editTP, name='editTP'),
    path('tutorProfileAvailability', views.tutorProfileAvailability.as_view(), name='tutorProfileAvailability'),
    path('editTPA', views.editTPA, name='editTPA'),
    path('tutorSchedule', views.tutorSchedule, name='tutorSchedule'),
    path('allTutors', views.allTutors, name='allTutors'),
]
