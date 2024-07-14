from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SingInForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField