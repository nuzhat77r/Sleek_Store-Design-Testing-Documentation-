"""
Registration Forms documentation
------------------------------------------

"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
Code Packages for registration forms

"""


class CustomerRegistrationForm(UserCreationForm):
    """
    This class is extended from the UserCreationForm class so it has all the functionality
    of the UserRegistrationForm class.
    this class used to create objects 
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
     model = User
     fields = ['username','email','password1','password2']
     labels = {'email':'Email'}
     widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}


