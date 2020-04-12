from django import forms

from .models import User

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'major', 'tsubjects', 'texp', 'hourlyRate']
        widgets = {
            'phone': forms.NumberInput(attrs={'class': "form-control"}),
            'major': forms.TextInput(attrs={'class': "form-control"}),
            'tsubjects': forms.TextInput(attrs={'class': "form-control"}),
            'texp': forms.TextInput(attrs={'class': "form-control"}),
            'hourlyRate': forms.NumberInput(attrs={'class': "form-control"}),
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
            'year': forms.NumberInput(attrs={'class':"form-control"}),
            'phone': forms.NumberInput(attrs={'class':"form-control"}),
            'classes': forms.TextInput(attrs={'class':"form-control"}),
            'major': forms.TextInput(attrs={'class':"form-control"})
        }
