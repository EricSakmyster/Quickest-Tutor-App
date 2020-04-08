from django import forms

from .models import User

class TutorProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['year','phone', 'tsubjects', 'major', 'texp', 'hourlyRate']

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
