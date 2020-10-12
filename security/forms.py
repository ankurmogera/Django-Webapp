#This file is used to create form that maps the model to HTML <input> elements
#Using built-in form class 'UserCreationForm to create our form
#Using built-in model 'User'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

