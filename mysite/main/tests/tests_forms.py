from django.test import TestCase
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
        
