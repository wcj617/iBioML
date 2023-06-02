from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)

    class Meta:
        model = Question
        fields = ['title', 'content']


class AnswerForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)

    class Meta:
        model = Answer
        fields = ['content']
