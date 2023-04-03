from django.db import models

# Create your models here.
class Example(models.Model):
    coursename = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
