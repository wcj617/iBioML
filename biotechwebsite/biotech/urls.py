from django.urls import path
from . import views

urlpatterns = [
    path('', views.htmlrender, name='htmlrender'),

    path('htmlrender/<int:question_id>/',
         views.htmlrender, name='htmlrender_with_id'),

    path('projects/', views.projectsrender, name='projectsrender'),

    path('contact/', views.contactrender, name='contactrender'),

    path('faculty/', views.facultyrender, name='facultyrender'),

    path('collaborators/', views.collabrender, name='collabrender'),

    path('mission/', views.missionrender, name='missionrender'),

    path('question/new/', views.question_create_view, name='create_question'),

    path('question/<int:question_id>/answer/',
         views.answer_create_view, name='create_answer'),

    path('genechat/', views.generender, name='generender'),

    path('profile/', views.profilerender, name='profilerender'),

    path('signup/', views.RegisterView.as_view(), name='users-register')

]
