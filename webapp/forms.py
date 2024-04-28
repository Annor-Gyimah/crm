from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Employee

# register a user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
  

# create employee
class add_employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['first_name', 'last_name','email', 'phone_number', 'address', 'city', 'country']


# update employee
class update_employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['first_name', 'last_name','email', 'phone_number', 'address', 'city', 'country']
