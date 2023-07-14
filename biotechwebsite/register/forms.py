from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from allauth.socialaccount.forms import SignupForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))

    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    ROLE_CHOICES = [
        ('domain_expert', 'Domain Expert'),
        ('practitioner', 'Practitioner'),
    ]
    role = forms.ChoiceField(
        choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'class-name'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            # Assign the user to the chosen group.
            group_name = self.cleaned_data.get(
                'role').replace('_', ' ').title()
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class MyCustomSocialSignupForm(SignupForm):

    ROLE_CHOICES = [
        ('domain_expert', 'Domain Expert'),
        ('practitioner', 'Practitioner'),
    ]
    role = forms.ChoiceField(
    choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'class-name'}))
    #
    def save(self, request):

        # Ensure you call parent class's save
        # .save() returns a User object

        user = super(MyCustomSocialSignupForm, self).save(request)
        print(request)
        # Add your own processing here
        user.role = self.cleaned_data['role']
        # You must return the original result
        user.save()
        group_name = self.cleaned_data.get('role').replace('_', ' ').title()
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        return user

