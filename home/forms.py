from django import forms

from .models import User

class TutorProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['year','phone', 'subjects', 'majors', 'experience', 'hourlyRate']