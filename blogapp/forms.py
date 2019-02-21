from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
   

    class Meta:
        model = customUser
        fields = ['username', 'email', 'password1', 'password2','user_image']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = customUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = customUser
        fields = ['user_image']        
