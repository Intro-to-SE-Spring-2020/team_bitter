from django.contrib import admin
from .models import Tutorial
from .models import Tweet
from django.db import models


class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title",
              "tutorial_published",
              "tutorial_content"
    ]


class TweetAdmin(admin.ModelAdmin):
    fields = [
              "tweet_content",
              "tweet_published",
              "user",
              ]

# Register your models here.
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Tweet, TweetAdmin)
