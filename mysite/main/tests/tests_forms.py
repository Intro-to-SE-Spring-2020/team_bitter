from django.test import TestCase
from main.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm	
from .models import Tweet	
from .forms import TweetForm	
from django.urls import reverse	

# Create your tests here.	

class TweetFormTest(TestCase):	

    def test_tweet_form(self):	
        form = TweetForm({	
            'tweet_content': "This is my first Tweet",	
            }, )	
        self.assertTrue(form.is_valid())	
        tweet = form.save()	
        self.assertEqual(tweet.tweet_content, 'This is my first Tweet')	

    def test_empty_tweet_form(self):	
        form = TweetForm({},)	
        self.assertFalse(form.is_valid())

	def test_new_user_form_valid_data(self):
		form = NewUserForm(data={
			'username': 'newuser',
			'first_name': 'John',
			'last_name': 'Smith',
			'email': 'abc@gmail.com',
			'password1': 'Abc123*sample',
			'password2': 'Abc123*sample'
			}) 
		self.assertTrue(form.is_valid())

	def test_new_user_forms_no_data(self):
		form = NewUserForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),6)

	def test_authenticate_forms_no_data(self):
		n_form = AuthenticationForm(data={})
		self.assertFalse(n_form.is_valid())
		self.assertEquals(len(n_form.errors),2)


