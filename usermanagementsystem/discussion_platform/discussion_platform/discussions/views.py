# discussion_platform/discussions/views.py

from rest_framework import generics
from .models import Discussion
from .serializers import DiscussionSerializer

class DiscussionListView(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DiscussionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
