from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
class Register(UserCreationForm):
    password1 = forms.CharField(
            label = 'Password',
            strip = False,
            widget = forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )
    password2 = forms.CharField(
            label = 'Confirm Password',
            strip = False,
            widget = forms.PasswordInput(attrs={'autocomplete':'new-password',}),
    )

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password1','password2')
        field_classes = {'username':UsernameField}
