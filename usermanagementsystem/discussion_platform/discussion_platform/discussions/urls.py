# discussion_platform/discussions/urls.py

from django.urls import path
from .views import DiscussionListView, DiscussionDetailView

urlpatterns = [
    path('discussions/', DiscussionListView.as_view(), name='discussion-list'),
    path('discussions/<int:pk>/', DiscussionDetailView.as_view(), name='discussion-detail'),
]
