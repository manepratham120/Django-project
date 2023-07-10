from django import forms
from todo_app.models import tasklists
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class taskform(forms.ModelForm):
    class Meta:
        model=tasklists
        fields= ['task','done']