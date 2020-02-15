from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

#SignUp Form w/email 
class SignUpForm(UserCreationForm):
    #Fields
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200) #not in default User Creation Form

    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean(self): #set clean function to validate that email isnt being reused
       email = self.cleaned_data.get('email') #get email
       if User.objects.filter(email=email).exists(): #raise validation error if email exists
            raise ValidationError({'email': ["Email already exist with another account. Please try a different email or password reset."]})
       return self.cleaned_data 
