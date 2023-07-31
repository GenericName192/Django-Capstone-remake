from django import forms
from .models import UserInfo, User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name", max_length=30)
    last_name = forms.CharField(label="Last name", max_length=30)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password1'
        self.fields['password1'].help_text = 'Your password can\'t be too similar to your other personal information. \nYour password must contain at least 8 characters. \nYour password can\'t be a commonly used password. \nYour password can\'t be entirely numeric.'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Password2'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

