from django import forms

from .models import User
from django.forms.widgets import FileInput

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'major', 'tsubjects', 'texp', 'hourlyRate']
        widgets = {
            'phone': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "XXX-XXX-XXXX"}),
            'major': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Math, Chemistry"}),
            'tsubjects': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Math, English"}),
            'texp': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Calc teacher 3 years"}),
            'hourlyRate': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "expected hourly pay"}),
        }
class TutorProfileAvailibilityForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['tutorAvailibility']
        widgets = {
            'tutorAvailibility': forms.DateTimeInput(attrs={'class': "form-control"}),
        }
class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['year','phone', 'classes', 'major']
        widgets={
            'year': forms.NumberInput(attrs={'class':"form-control", 'placeholder': "1,2,3,or 4"}),
            'phone': forms.NumberInput(attrs={'class':"form-control", 'placeholder': "XXX-XXX-XXXX"}),
            'classes': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, English"}),
            'major': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, Chemistry"})
        }