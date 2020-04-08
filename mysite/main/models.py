from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.tutorial_title

#This class creates a table in SQLite for the Tweets    
class Tweet(models.Model):
    tweet_content = models.CharField(max_length = 280)
    tweet_published = models.DateTimeField('date published', default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)
                                           
    def __str__(self):
        return self.tweet_content
class UserRelationship(models.Model):
    selfname=models.CharField(max_length=50)
    friendname=models.CharField(max_length=50)
class UserBlocked(models.Model):
    selfname=models.CharField(max_length=50)
    blockname=models.CharField(max_length=50)
