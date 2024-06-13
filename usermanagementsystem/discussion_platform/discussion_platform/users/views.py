# discussion_platform/users/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchUserView(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        if name:
            users = User.objects.filter(username__icontains=name)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response("Please provide a 'name' parameter for searching.", status=status.HTTP_400_BAD_REQUEST)
