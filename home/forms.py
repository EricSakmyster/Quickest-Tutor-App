from django import forms

from .models import User, Available, RequestSession

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'major', 'tsubjects', 'texp', 'hourlyRate', 'image']
        widgets = {
            'phone': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "01234567890"}),
            'major': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Math, Chemistry"}),
            'tsubjects': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Math, English"}),
            'texp': forms.TextInput(attrs={'class': "form-control", 'placeholder': "ex) Calc teacher 3 years"}),
            'hourlyRate': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "expected hourly pay"}),
        }
class TutorProfileAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Available
        fields = ['available']
        widgets = {
            'available': forms.DateTimeInput(attrs={'class': "form-control", 'title': 'MM/DD/YYYY HH:MM'}),
        }
class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['year','phone', 'classes', 'major']
        widgets={
            'year': forms.NumberInput(attrs={'class':"form-control", 'placeholder': "1,2,3,or 4"}),
            'phone': forms.NumberInput(attrs={'class':"form-control", 'placeholder': "01234567890"}),
            'classes': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, English"}),
            'major': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, Chemistry"})
        }

class SessionRequestForm(forms.ModelForm):
    
    class Meta:
        model = RequestSession
        fields = ['student_availability','students_class', 'note']
        widgets={
            'student_availability': forms.DateTimeInput(attrs={'class': "form-control", 'title': 'MM/DD/YYYY HH:MM'}),
            'students_class': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Ex) CS1110"}),
            'note': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Notes"})
        }
