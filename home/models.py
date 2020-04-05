import datetime
from django.urls import reverse

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name


class Student(models.Model):
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.year

class Tutor(models.Model):
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.year


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.date.today)


def __str__(self):
    return self.title


@property
def get_html_url(self):
    url = reverse('event_edit', args=(self.id,))
    return f'<p>{self.title}</p><a href="{url}">edit</a>'


class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar
    objects = models.Manager()

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class TodoList(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
