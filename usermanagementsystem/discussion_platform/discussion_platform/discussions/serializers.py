# discussion_platform/discussions/serializers.py

from rest_framework import serializers
from .models import Discussion

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('id', 'text', 'image', 'created_on')
