from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import Question, Answer, QuestionForm, AnswerForm
from .models import Question, Answer, QuestionFile, AnswerFile


def htmlrender(request, question_id=None):
    content = {
        'title': 'Welcome to the cutting-edge intersection of computer science and biotechnology at the University of Washington Bothell!',
        'paragraphs': [
            'Our passionate team of researchers and computer scientists is dedicated to exploring and advancing the fields of bioinformatics, systems biology, and computational biology. By harnessing the power of mathematics, statistics, computer science, and engineering, we develop innovative algorithms and sophisticated software programs to delve deep into the vast, complex world of biological data.',
            'The management and analysis of intricate biological data sets present both an immense challenge and an extraordinary research opportunity. As such, our primary research focus lies in pattern recognition within bioinformatics, specifically in the realm of biological motif analysis. Through our work, we strive to unveil hidden patterns, discover meaningful insights, and unlock the full potential of biological data, ultimately contributing to the betterment of human health, environmental sustainability, and global progress.',
            'Join us as we embark on this exciting journey at the forefront of computational biology, pushing the boundaries of knowledge and innovation in our relentless pursuit of excellence.'
        ]
    }
    return render(request, 'template-kush.html', {'content': content})


def projectsrender(request):
    return render(request, 'projects/projects.html')


# def loginrender(request):
#     return render(request, 'registration/login.html')


def contactrender(request):
    return render(request, 'contact/contact-kush.html')


def facultyrender(request):
    return render(request, 'static/people/core-faculty.html')


def collabrender(request):
    return render(request, 'static/people/collab.html')


def missionrender(request):
    return render(request, 'static/mission/mission.html')


def generender(request):
    questions = Question.objects.all()
    return render(request, 'gene-chat.html', {'questions': questions})


def question_create_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            # question.given_to = request.user
            question.save()

            for f in request.FILES.getlist('file_field'):
                QuestionFile.objects.create(file=f, question=question)

            return redirect('generender')
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})


def answer_create_view(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_by = request.user
            answer.question = question
            answer.save()

            for f in request.FILES.getlist('file_field'):
                AnswerFile.objects.create(file=f, answer=answer)

            return redirect('htmlrender', question_id=question_id)
    else:
        form = AnswerForm()
    return render(request, 'create_answer.html', {'form': form})
