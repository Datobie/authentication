from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="Please enter a valid email address"),
    # Bio = forms.CharField(max_length=400)
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]