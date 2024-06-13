from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, HashTag, Discussion, Comment, Like
from .serializers import UserSerializer, HashTagSerializer, DiscussionSerializer, CommentSerializer, LikeSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchUserView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return User.objects.filter(username__icontains=name)
        return User.objects.all()

class CreateDiscussionView(generics.CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class UpdateDiscussionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class DeleteDiscussionView(generics.DestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

class ListDiscussionByTagView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag', None)
        if tag:
            return Discussion.objects.filter(hashtags__name__icontains=tag)
        return Discussion.objects.all()

class ListDiscussionByTextView(generics.ListAPIView):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        text = self.request.query_params.get('text', None)
        if text:
            return Discussion.objects.filter(text__icontains=text)
        return Discussion.objects.all()

class FollowUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = self.request.user
        try:
            target_user = User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.following.add(target_user)
        return Response(status=status.HTTP_200_OK)

class UnfollowUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = self.request.user
        try:
            target_user = User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.following.remove(target_user)
        return Response(status=status.HTTP_200_OK)

class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeCommentView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        try:
            comment = Comment.objects.get(id=self.kwargs['pk'])
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        Like.objects.create(user=user, comment=comment)
        return Response(status=status.HTTP_201_CREATED)

class UnlikeCommentView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        try:
            comment = Comment.objects.get(id=self.kwargs['pk'])
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        Like.objects.filter(user=user, comment=comment).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IncrementViewCountView(generics.RetrieveAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def get(self, request, *args, **kwargs):
        discussion = self.get_object()
        discussion.view_count += 1
        discussion.save()
        serializer = self.get_serializer(discussion)
        return Response(serializer.data)
