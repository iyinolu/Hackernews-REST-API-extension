from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class Story(models.Model):
    STORY_TYPES = [
        ("job", "Job"),
        ("story", "Story"),
        ("comment", "Comment"),
        ("poll", "Poll"),
        ("pollopt", "Poll Option")
    ]

    storyId = models.IntegerField(unique=True, null=False, blank=False)
    type = models.CharField(max_length=10, choices=STORY_TYPES, null=False, blank=False)
    title = models.CharField(null=True, blank=True, max_length=200)
    text = models.CharField(null=True, blank=True, max_length=10000)
    url = models.CharField(null=True, blank=True, max_length=500)
    
    def __str__(self):
        return "%s" % (self.title)

class Comments(models.Model):
    commentId = models.IntegerField(unique=True, null=False, blank=False)
    text = models.CharField(null=True, blank=True, max_length=5000)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    