from django import forms
from .models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username' , 'password1', 'password2']
