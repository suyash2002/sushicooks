from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser
#if we want to add fields to our user login/signup form we can
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields