from django.urls import path
from . import views

urlpatterns = [
    path('', views.htmlrender, name='htmlrender'),
    path('projects/', views.projectsrender, name='projectsrender'),
    path('login/', views.loginrender, name='loginrender'),
    path('contact/', views.contactrender, name='contactrender'),
    path('faculty/', views.facultyrender, name='facultyrender'),
    path('collaborators/', views.collabrender, name='collabrender'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('mission/', views.missionrender, name='missionrender'),
]
