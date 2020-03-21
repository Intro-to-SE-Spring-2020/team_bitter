from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.tutorial_title
    
class Tweet(models.Model):
    #tweet_id = models.AutoField(primary_key = True)
    tweet_content = models.CharField(max_length = 280)
    tweet_published = models.DateTimeField('date published', default=datetime.now)
    #user = models.ForeignKey(User)
    
    def __str__(self):
        return self.tweet_content
