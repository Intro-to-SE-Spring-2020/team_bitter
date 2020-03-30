from django.test import TestCase
from .models import Tweet

# Create your tests here.

class TweetModelTest(TestCase):
    def setUp(self):
        Tweet.objects.create(tweet_content='Hello, this is my first tweet.')


    def test_tweet(self):
        tweet = Tweet.objects.get(id=1)
        field_label = tweet._meta.get_field('tweet_content').verbose_name
        self.assertEquals(field_label, 'tweet content')


    def test_tweet_published(self):
        tweet = Tweet.objects.get(id=1)
        field_label = tweet._meta.get_field('tweet_published').verbose_name
        self.assertEquals(field_label, 'date published')


    def test_tweet_length(self):
        tweet = Tweet.objects.get(id=1)
        max_length = tweet._meta.get_field('tweet_content').max_length
        self.assertEquals(max_length, 280)

    
