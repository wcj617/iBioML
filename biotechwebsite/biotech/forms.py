from django import forms
from .models import Question, Answer, Student, Practitioner
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'file']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'file']
