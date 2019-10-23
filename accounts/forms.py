from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """ Form to register a new user to User table """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """ Form to update User info username and email """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """ Form to update Profile info """
    class Meta:
        model = Profile
        fields = ['address_line_1', 'address_line_2', 'town_or_city', 'county', 'postcode', 'country']