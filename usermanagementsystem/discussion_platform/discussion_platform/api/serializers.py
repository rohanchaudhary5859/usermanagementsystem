from rest_framework import serializers
from .models import User, Discussion, Comment, Like, HashTag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobile_no', 'email', 'followers', 'following']

class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ['id', 'name']

class DiscussionSerializer(serializers.ModelSerializer):
    hashtags = HashTagSerializer(many=True)
    
    class Meta:
        model = Discussion
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_on', 'view_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'discussion', 'text', 'created_on', 'parent']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'comment', 'created_on']
