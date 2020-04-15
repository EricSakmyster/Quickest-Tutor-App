from django import forms

from .models import User, Available, RequestSession

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'major', 'tsubjects', 'texp', 'hourlyRate', 'image']
        widgets = {
            'phone': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "XXX-XXX-XXXX"}),
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
            'phone': forms.NumberInput(attrs={'class':"form-control", 'placeholder': "XXX-XXX-XXXX"}),
            'classes': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, English"}),
            'major': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) Math, Chemistry"})
        }

class SessionRequestForm(forms.ModelForm):
    
    class Meta:
        model = RequestSession
        fields = ['student_availability', 'tutor_username', 'course', 'description']
        widgets={
            'student_availability': forms.DateTimeInput(attrs={'class': "form-control", 'title': 'MM/DD/YYYY HH:MM', 'placeholder': "What time works for you? (MM/DD/YYYY HH:MM)"}),
            'tutor_username': forms.HiddenInput(),
            'course': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) CS 2150"}),
            'description': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Describe what you need to be tutored for"}),
        }
class SessionOptionForm(forms.ModelForm):
    
    class Meta:
        model = RequestSession
        fields = ['student_availability', 'tutor_username', 'course', 'description', 'is_accepted']
        widgets={
            'student_availability': forms.DateTimeInput(attrs={'class': "form-control", 'title': 'MM/DD/YYYY HH:MM', 'placeholder': "What time works for you? (MM/DD/YYYY HH:MM)"}),
            'tutor_username': forms.HiddenInput(),
            'course': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) CS 2150"}),
            'description': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Describe what you need to be tutored for"}),
            'is_accepted': forms.BooleanField(),
        }
