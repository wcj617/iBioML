from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label="New username",
        # help_text="Your custom help text for the username field.",
        widget=forms.TextInput(attrs={'class': 'custom-input'})
    )
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'custom-input'}),
        # help_text="Your custom help text for the password field.",
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'custom-input'}),
        # help_text="Your custom help text for the password confirmation field.",
    )
