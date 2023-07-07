from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_questions')
    given_to = models.ForeignKey(
        User, unique=False, on_delete=models.CASCADE, related_name='received_questions', null=True)
    posted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


class QuestionFile(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file = models.FileField(upload_to='questions_files/')


class AnswerFile(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    file = models.FileField(upload_to='answers_files/')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(
    #     default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
