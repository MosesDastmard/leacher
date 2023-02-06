from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
                    'username': forms.fields.TextInput(attrs={'placeholder': 'Username'}),
                    'email': forms.fields.TextInput(attrs={'placeholder': 'Email'}),
                    'password1': forms.fields.TextInput(attrs={'placeholder': 'Password'}),
                    'password2': forms.fields.TextInput(attrs={'placeholder': 'Confirm Password'}),
                }