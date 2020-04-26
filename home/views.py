from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import TutorProfileForm, TutorProfileAvailabilityForm, StudentProfileForm, SessionRequestForm

from .models import TodoList, Category, User, Available, RequestSession


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def signin(request):
    return render(request, 'home/signIn.html')


class WelcomeView(generic.TemplateView):
    model = User
    template_name = 'home/welcome.html'
    context_object_name = 'user'


def profile(request):
    return render(request, 'home/studentProfile.html')


def editSP(request):
    if request.method == "POST":
        sform = StudentProfileForm(request.POST, instance=request.user)
        if sform.is_valid():
            post = sform.save(commit=False)
            post.year = request.user.year
            post.phone = request.user.phone
            post.classes = request.user.classes
            post.major = request.user.major
            post.save()
            return redirect('profile')
    else:
        sform = StudentProfileForm(instance=request.user)
    return render(request, 'home/editSP.html', {'sform': sform})


def locateSessions(request):
    studentAcceptedSessions = RequestSession.objects.filter(student_id=request.user.id, is_accepted=True)
    tutorAcceptedSessions = RequestSession.objects.filter(tutor_id=request.user.id, is_accepted=True)
    if request.method=="POST":
        if "View Student Sessions" in request.POST:
            context = {'AcceptedSessions': studentAcceptedSessions}
            return render(request, 'home/locateSessions.html', context)
        if "View Tutor Sessions" in request.POST:
            context = {'AcceptedSessions': tutorAcceptedSessions}
            return render(request, 'home/locateSessions.html', context)
    context = {'AcceptedSessions': studentAcceptedSessions}
    return render(request, 'home/locateSessions.html', context)


class tutorProfile(generic.TemplateView):
    model = User
    template_name = 'home/tutorProfile.html'
    context_object_name = 'thisTutor'

class tutorProfileAvailability(generic.TemplateView):
    model = User
    template_name = 'home/tutorProfileAvailability.html'
    context_object_name = 'thistutor'

def editTPA(request):
    userObject = User.objects.get(username = request.user.username)
    if request.method=="POST":
        tpaform = TutorProfileAvailabilityForm(request.POST)
        if tpaform.is_valid():
            post=tpaform.save(commit=False)
            post.available=tpaform.cleaned_data['available']
            userObject.tutorAvailability.append(tpaform.cleaned_data['available'])
            userObject.save()
            return redirect('tutorProfileAvailability')
    else:
        tpaform = TutorProfileAvailabilityForm()
    return render(request, 'home/editTPA.html', {'tpaform': tpaform})

def editTP(request):
    if request.method == "POST":
        tform = TutorProfileForm(request.POST, instance=request.user)
        if tform.is_valid():
            post = tform.save(commit=False)
            post.phone = request.user.phone
            post.major = request.user.major
            post.tsubjects = request.user.tsubjects
            post.texp = request.user.texp
            post.hourlyRate = request.user.hourlyRate
            post.save()
            return redirect('tutorProfile')
    else:
        tform = TutorProfileForm(instance=request.user)
    return render(request, 'home/editTP.html', {'tform': tform})


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    # tutorRequestedSessions = RequestSession.objects.filter(tutor_id=request.user.id)
    # context = {'sessions': tutorRequestedSessions}
    # tutorRequestedSessions = RequestSession.objects.filter(tutor_id=request.user.id)
    tutorAcceptedSessions =  RequestSession.objects.filter(is_accepted=True)
    context = {'tutorAcceptedSessions': tutorAcceptedSessions}
    mapbox_access_token = 'pk.my_mapbox_access_token'

    return render(request, 'locateSessions.html',
                  {
                      'mapbox_access_token': 'pk.eyJ1IjoiZXJpY3Nha215c3RlciIsImEiOiJjazhiMXlxZmUwMWN0M2VxZWp2cGIwcGE3In0.LOR2DgUVncLrbVuaPtD5QA'},context)

'''
def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/studentSchedule")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "home/studentSchedule.html", {"todos": todos, "categories": categories})
'''
def allTutors(request):
    
    if request.method == "POST":
        srform = SessionRequestForm(request.POST, instance=request.user)
        if srform.is_valid():
            post = srform.save(commit=False)
            post.student_availability= srform.cleaned_data['student_availability']
            post.course = srform.cleaned_data['course']
            post.description = srform.cleaned_data['description']
            tu=srform.cleaned_data['tutor_username']
            post.tutor_username = tu
            # post.location = srform.cleaned_data['building']

            post.save()
            
            request = RequestSession(student_availability=srform.cleaned_data['student_availability'], course=srform.cleaned_data['course'], description=srform.cleaned_data['description'], tutor_username=tu, student=User.objects.get(username = request.user.username), tutor =User.objects.get(username = tu), is_accepted=False, building=srform.cleaned_data['building'])
            request.save()
            # if request.is_accepted:
            #     request.tutor.location = request.building
            return redirect('allTutors')
    else:
        srform = SessionRequestForm(instance=request.user)
    tutors = get_user_model().objects.all()
    context = {'tutors': tutors, 'srform': srform}
    return render(request, 'home/allTutors.html', context)

def studentSchedule(request):
    studentRequestedSessions = RequestSession.objects.filter(student_id=request.user.id)
    tutorAcceptedSessions = studentRequestedSessions.filter(is_accepted=True)
    studentRequestedSessions = studentRequestedSessions.filter(is_accepted=False)
    context = {'studentRequestedSessions': studentRequestedSessions, 'tutorAcceptedSessions': tutorAcceptedSessions}
    return render(request, 'home/studentSchedule.html', context)

def tutorSchedule(request):

    tutorRequestedSessions = RequestSession.objects.filter(tutor_id=request.user.id)
    tutorAcceptedSessions = tutorRequestedSessions.filter(is_accepted=True)
    tutorRequestedSessions = tutorRequestedSessions.filter(is_accepted=False)
    context = {'tutorRequestedSessions': tutorRequestedSessions, 'tutorAcceptedSessions': tutorAcceptedSessions}
    if request.method=="POST":
        if "Accept" in request.POST:
            acceptedSession=RequestSession.objects.get(id=request.POST["id"])
            acceptedSession.is_accepted=True
            acceptedSession.save()

        if "Decline" in request.POST:
            RequestSession.objects.get(id=request.POST["id"]).delete()
    return render(request, 'home/baseTutor.html', context)
