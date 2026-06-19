from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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