# discussion_platform/users/urls.py

from django.urls import path
from .views import UserListView, UserDetailView, SearchUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/search/', SearchUserView.as_view(), name='user-search'),
]
