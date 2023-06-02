from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='questions_files/')
    posted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file = models.FileField(upload_to='answers_files/')
    posted_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_code = models.CharField(max_length=30)


class Practitioner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_code = models.CharField(max_length=30)
