from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'home/signIn.html')

def welcome(request):
    return render(request, 'home/welcome.html')

def profile(request):
    return render(request, 'home/studentProfile.html')

def studentSchedule(request):
    return render(request, 'home/studentSchedule.html')

def tutorsearch(request):
    return render(request, 'home/tutorSearch.html')

def tutorProfile(request):
    return render(request, 'home/tutorProfile.html')

def editTP(request):
    return render(request, 'home/editTP.html')

def tutorSchedule(request):
    return render(request, 'home/baseTutor.html')

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'tutorSearch.html', 
                  { 'mapbox_access_token': 'pk.eyJ1IjoiZXJpY3Nha215c3RlciIsImEiOiJjazhiMXlxZmUwMWN0M2VxZWp2cGIwcGE3In0.LOR2DgUVncLrbVuaPtD5QA'})

def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/studentSchedule") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "home/studentSchedule.html", {"todos": todos, "categories":categories})