from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
     """
    This form is used to create a new registration form for customer.
    This form consists of three fields.
     - username: The title of the user.
     - email: The email id of user.
     - password: The password of user.
     
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
     model = User
     fields = ['username','email','password1','password2']
     labels = {'email':'Email'}
     widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
     """
    This form is used to create a new login form for customer.
    This form consists of two fields.
     - username: The title of the user.
     - password: The password of user.
     
    """
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
     """
    This form is used to create a new password change form for customer.
    This form consists of three fields.
     - username: The title of the user.
     - new_password1: The new pass1 for user.
     - new_password1: The new pass1 for user.
     - old_password1: The old password of user.
     
    """
    old_password = forms.CharField(label=_("Old Password"),
    strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
     """
    This form is used to reset password for customer.
    This form consists of two fields.
     - email: User email
     -email_Input: New input
     
    """
    email =forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email','class':'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
      """
    This form is used to reset password for customer.
    This form consists of two fields.
     - email: User email
     -email_Input: New input
     
    """
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
     """
    This form is used to create a form for customer.
    This form consists of five fields.
     - name: The title of the user.
     - locality: The locality of user.
     - zipcode: The zipcode of user.
     - division: division of user
     
    """
    class Meta:
        model = Customer
        fields =['name','locality','city','zipcode','division']
        widgets = {'name':forms.TextInput(attrs= {'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}), 'division':forms.Select(attrs={'class':'form-control'}), 'zipcode':forms.NumberInput(attrs={'class':'form-control'})}

