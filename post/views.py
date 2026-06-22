from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Post
from .serializers import PostSerializer
class PostListCreateAPIView(APIView):


    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PostDetailAPIView(APIView):

    def get_object(self, pk):
        return Post.objects.get(id=pk)

    def get(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(
            post,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        post = self.get_object(pk)

        post.delete()

        return Response(
            {"message": "Post o'chirildi"},
            status=status.HTTP_204_NO_CONTENT
        )

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegisterAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response(
                {'error': 'Parollar mos emas'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User(username=username)
        user.set_password(password)
        user.save()

        return Response(
            {'message': 'User yaratildi'},
            status=status.HTTP_201_CREATED
        )
class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return Response(
                {'message': 'Login successful'}
            )

        return Response(
            {'error': 'Login yoki parol xato'},
            status=status.HTTP_400_BAD_REQUEST
        )
class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)

        return Response(
            {'message': 'Logout successful'}
        )


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]