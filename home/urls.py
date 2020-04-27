from django.urls import path

from . import views

from .views import studentSessionDelete, tutorSessionDelete, UserListView

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    path('welcome', views.WelcomeView.as_view(), name='welcome'),
    path('signin', views.signin, name='signin'),
    path('studentProfile', views.profile, name='profile'),
    path('editSP', views.editSP, name='editSP'),
    path('studentSchedule', views.studentSchedule, name='schedule'),
    path('studentLocateSessions', views.studentLocateSessions, name='studentLocateSessions'),
    path('tutorLocateSessions', views.tutorLocateSessions, name='tutorLocateSessions'),
    path('tutorProfile', views.tutorProfile.as_view(), name='tutorProfile'),
    path('editTP', views.editTP, name='editTP'),
    path('tutorProfileAvailability', views.tutorProfileAvailability, name='tutorProfileAvailability'),
    path('editTPA', views.editTPA, name='editTPA'),
    path('tutorSchedule', views.tutorSchedule, name='tutorSchedule'),
    path('allTutors', UserListView.as_view(), name='allTutors'),
    path('<pk>/student/delete/', studentSessionDelete.as_view(), name='studentSession-delete'),
    path('<pk>/tutor/delete/', tutorSessionDelete.as_view(), name='tutorSession-delete'),
]
