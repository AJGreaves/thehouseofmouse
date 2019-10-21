from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    """
    Default django user creation form but make email address field required.
    example code used for reference by fellow student Robin Zigmond
    https://github.com/robinzigmond/chamber_mates/blob/master/accounts/forms.py
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name" "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = True
