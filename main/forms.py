from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import User, Profile, Comment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_pic', 'nickname']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

