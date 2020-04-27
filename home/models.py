import datetime
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator 


class User(AbstractUser):
    # BUILDING_CHOICES =( 
    #     ("1", "Aldernman"), 
    #     ("2", "Shannon"), 
    #     ("3", "Rice"), 
    # ) 
    year = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    phone_regex = RegexValidator(regex=r'^(\d{3}\-\d{3}\-\d{4})$', message="Phone number must be entered in the format: '999-999-9999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    classes = models.TextField(max_length=100, default='none')
    major = models.TextField(max_length=20, default='none')
    tsubjects = models.TextField(max_length=500, default='none')
    texp = models.TextField(max_length=500, default='none')
    hourlyRate = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    requests = models.ManyToManyField("RequestSession", blank=True)
    tutorAvailability = ArrayField(models.DateTimeField(default=datetime.now, blank=True), default=list, blank=True)
    pfp = models.ImageField(blank= True, null= True)
    location = models.CharField(max_length=100, default='')

    # building = ArrayField(models.CharField(max_length=32, blank=True, choices=BUILDING_CHOICES), blank = True, default=list)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class RequestSession(models.Model):
    objects = models.Manager()
    chosen_time = models.TextField(max_length=100, default='none')
    tutor_username = models.TextField(max_length=20, default='none')
    description = models.TextField(max_length=50, default='')
    course = models.TextField(max_length=20, default='')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', default=1)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor', default=1)
    is_accepted = models.BooleanField(default=False)
    building = models.CharField(max_length=100, default='')
   
    def __str__(self):
        return self.description
        
class Available(models.Model):
    available = models.DateTimeField(default=datetime.now, blank=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.available)


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
