from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms #for widgets text input, email input
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from . models import Record

class CreateUserForm(UserCreationForm):
    class Meta:
        # this one comes from django by default
        model = User
        # the second one is for confirmation
        fields = ['username', 'password1', 'password2'] 
        

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# A form to add in records
# note how we use the model we had created
# Create
class CreateRecordForm(forms.ModelForm):
    class Meta:
        # import the record model
        model = Record
        # has to be in correct order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
    
    
# Update
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']