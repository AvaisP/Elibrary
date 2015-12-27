from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields=('username','password','email','first_name','last_name',)

class UserFormRegister(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('SapID', )        