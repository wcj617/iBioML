from django.urls import path
from . import views

urlpatterns = [
            path('', views.htmlrender, name = 'htmlrender'),
            path('projects/', views.projectsrender, name = 'projectsrender'),
            path('login/', views.loginrender, name = 'loginrender'),
            path('signup/', views.signuprender, name = 'signuprender'),
            path('contact/', views.contactrender, name = 'contactrender')
        ]