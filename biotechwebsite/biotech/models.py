from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class Example(models.Model):
    coursename = models.CharField(max_length=10)
    major = models.CharField(max_length=20)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    stuff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'stuff', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Invalid email format')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    Search = forms.CharField(max_length=100)


