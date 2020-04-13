import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime 


class User(AbstractUser):
    year = models.IntegerField(default='0')
    phone = models.TextField(max_length=20, default='0000000000')
    classes = models.TextField(max_length=100, default='none')
    major = models.TextField(max_length=20, default='none')
    tsubjects = models.TextField(max_length=500, default='none')
    texp = models.TextField(max_length=500,default='none')
    hourlyRate= models.TextField(max_length=20,default='none')
    emailAddress = models.TextField(max_length=50,default='none')
    def __str__(self):
        return str(self.first_name)+' '+ str(self.last_name)

class Available(models.Model):
    available=models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="general")
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
