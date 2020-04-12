from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import TutorProfileForm, TutorProfileAvailibilityForm, StudentProfileForm

from .models import TodoList, Category, User


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


def studentSchedule(request):
    return render(request, 'home/studentSchedule.html')


def tutorsearch(request):
    return render(request, 'home/tutorSearch.html')


class tutorProfile(generic.TemplateView):
    model = User
    template_name = 'home/tutorProfile.html'
    context_object_name = 'thisTutor'


class tutorProfileAvailibility(generic.TemplateView):
    model = User
    template_name = 'home/tutorProfileAvailibility.html'
    context_object_name = 'thisTutor'


def editTPA(request):
    if request.method == "POST":
        tpaform = TutorProfileAvailibilityForm(request.POST, instance=request.user)
        if tpaform.is_valid():
            post = tpaform.save(commit=False)
            post.tutorAvailibility = request.user.tutorAvailibility
            post.save()
            return redirect('tutorProfileAvailibility')
    else:
        tpaform = TutorProfileAvailibilityForm(instance=request.user)
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


def tutorSchedule(request):
    return render(request, 'home/baseTutor.html')


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'tutorSearch.html',
                  {
                      'mapbox_access_token': 'pk.eyJ1IjoiZXJpY3Nha215c3RlciIsImEiOiJjazhiMXlxZmUwMWN0M2VxZWp2cGIwcGE3In0.LOR2DgUVncLrbVuaPtD5QA'})


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


def allTutors(request):
    
    tutors = get_user_model().objects.all()
    context = {'tutors': tutors}
    return render(request, 'home/allTutors.html', context)
