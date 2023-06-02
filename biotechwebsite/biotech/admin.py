from django.contrib import admin
from .models import Question, Answer

# admin.site.register(Example)
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
