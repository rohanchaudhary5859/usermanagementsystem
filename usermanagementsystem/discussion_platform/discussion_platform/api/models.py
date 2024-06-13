from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    text = models.TextField()
    image = models.ImageField(upload_to='discussions/', blank=True, null=True)
    hashtags = models.ManyToManyField(HashTag, related_name='discussions')
    created_on = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    created_on = models.DateTimeField(auto_now_add=True)
