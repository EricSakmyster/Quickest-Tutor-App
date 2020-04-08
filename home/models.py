import datetime
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    year = models.IntegerField(default='0')
    phone = models.TextField(max_length=20, default='000-000-0000')
    classes = models.TextField(max_length=100, default='none')
    major = models.TextField(max_length=20, default='none')
    tsubjects = models.TextField(max_length=500, default='none')
    texp = models.TextField(max_length=500,default='none')
    hourlyRate= models.TextField(max_length=20,default='none')
    emailAddress = models.TextField(max_length=50,default='none')
    def __str__(self):
        return str(self.first_name)+' '+ str(self.last_name)


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.date.today)


def __str__(self):
    return self.title


@property
def get_html_url(self):
    url = reverse('event_edit', args=(self.id,))
    return f'<p>{self.title}</p><a href="{url}">edit</a>'


class Category(models.Model): 
    name = models.CharField(max_length=100)  
    objects = models.Manager()

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name 


class TodoList(models.Model): 
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True)  
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")  

    class Meta:
        ordering = ["-created"]  

    def __str__(self):
        return self.title  
