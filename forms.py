from django import forms
from django.contrib.auth.forms import  AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.utils.translation import gettext, gettext_lazy as _




class LoginForm(AuthenticationForm):
    """
    This class is extended from the AuthenticationForm class so it has all the functionality
    of the model class.
    this class used to create objects for database entry
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



