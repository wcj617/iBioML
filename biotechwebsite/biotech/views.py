from django.shortcuts import render
from django.http import HttpResponse
from biotech.models import RegisterForm

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/l-kush.html"

from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('success')
    template_name = 'registration/l-kush.html'


def htmlrender(request):
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


def loginrender(request):
    return render(request, 'registration/login.html')


def contactrender(request):
    return render(request, 'contact/contact-kush.html')


def facultyrender(request):
    return render(request, 'static/people/core-faculty.html')


def collabrender(request):
    return render(request, 'static/people/collab.html')


def missionrender(request):
    return render(request, 'static/mission/mission.html')
