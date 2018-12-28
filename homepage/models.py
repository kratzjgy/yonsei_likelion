from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Homepage(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length = 10, null=True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    published_date = models.DateTimeField(blank = True, null = True)
    hits = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length = 10)
    message = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.message
    
