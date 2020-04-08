from django import forms

from .models import User

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['emailAddress','year','phone', 'tsubjects', 'major', 'texp', 'hourlyRate', ]

class StudentProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['year','phone', 'major',]
