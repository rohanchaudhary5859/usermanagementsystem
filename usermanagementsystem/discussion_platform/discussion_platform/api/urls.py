from django.urls import path
from .views import (
    CreateUserView, UpdateUserView, DeleteUserView, ListUserView, SearchUserView,
    CreateDiscussionView, UpdateDiscussionView, DeleteDiscussionView, ListDiscussionByTagView,
    ListDiscussionByTextView, FollowUserView, UnfollowUserView, CreateCommentView, UpdateCommentView,
    LikeCommentView, UnlikeCommentView, IncrementViewCountView
)

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('users/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('users/delete/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('users/list/', ListUserView.as_view(), name='list-users'),
    path('users/search/', SearchUserView.as_view(), name='search-user'),

    path('discussions/', CreateDiscussionView.as_view(), name='create-discussion'),
    path('discussions/<int:pk>/', UpdateDiscussionView.as_view(), name='update-discussion'),
    path('discussions/delete/<int:pk>/', DeleteDiscussionView.as_view(), name='delete-discussion'),
    path('discussions/by-tag/', ListDiscussionByTagView.as_view(), name='list-discussion-by-tag'),
    path('discussions/by-text/', ListDiscussionByTextView.as_view(), name='list-discussion-by-text'),

    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),

    path('comments/', CreateCommentView.as_view(), name='create-comment'),
    path('comments/<int:pk>/', UpdateCommentView.as_view(), name='update-comment'),

    path('comments/like/<int:pk>/', LikeCommentView.as_view(), name='like-comment'),
    path('comments/unlike/<int:pk>/', UnlikeCommentView.as_view(), name='unlike-comment'),

    path('discussions/view/<int:pk>/', IncrementViewCountView.as_view(), name='increment-view-count'),
]
