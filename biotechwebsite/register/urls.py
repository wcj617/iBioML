from django.urls import path, include
from .views import RegisterView, CustomLoginView  # Import the view here
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='users-register'),  # This is what we added

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),
    # I think this cause the issues
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('', include('allauth.urls')),

    # path('is_open_for_signup/', views.accept_invitation, name='is_open_for_signup'),
]