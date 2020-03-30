from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Tweet
from datetime import datetime

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name= self.cleaned_data["first_name"]
        user.last_name= self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

#This class creates a form for the user to input a tweet to post on the homepage.
class TweetForm(forms.ModelForm):
    tweet_content = forms.CharField(max_length = 280)
    

    class Meta:
       model = Tweet
       widgets={
          "tweet_content": forms.TextInput()
          }
       fields = ('tweet_content',)

    

        

    

   
        
