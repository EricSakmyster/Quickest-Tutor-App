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
            'available': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'}),
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
        fields = ['tutor_username', 'course', 'description', 'building']

        BUILDING_CHOICES =( 
    ('initial', "Choose your Location"),
    ("Alderman Library", "Alderman Library"), 
    ("Clemons Library", "Clemons Library"), 
    ("Clark Library", "Clark Library"), 
    ("Thornton Stacks", "Thornton Stacks"), 
    ("Rice Hall", "Rice Hall"), 
    ("CDE", "CDE"), 
    ("Multicultural Student Center", "Multicultural Student Center"), 
    ("New Cabell", "New Cabell"), 
)
        widgets={
            'tutor_username': forms.HiddenInput(),
            'course': forms.TextInput(attrs={'class':"form-control", 'placeholder': "ex) CS 2150"}),
            'description': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Describe what you need to be tutored for"}),
            'building': forms.Select(attrs={'class': 'form-control'}, choices=BUILDING_CHOICES),
        }
