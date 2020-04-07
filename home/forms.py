from django.forms import ModelForm
from .models import TodoList, Category, User, Student, Tutor


class SuggestionForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"