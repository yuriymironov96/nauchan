from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import Board, Thread, Post
from serializers import ThreadSerializer, PostSerializer

# Create your views here.
class ThreadListView(APIView):
    serializer_class = ThreadSerializer

    def get(self, request, board, format=None):
        threads = Thread.objects.filter(board=get_object_or_404(Board,
                                    short_name=board)).all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)

    def post(self, request, board, format=None):
        serializer = PostSerializer(data=request.data, context={'board':board})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThreadView(APIView):
    serializer_class = PostSerializer

    def get(self, request, board, thread_id, format=None):
        posts = get_list_or_404(Post, thread_id=thread_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, board, thread_id, format=None):
        serializer = PostSerializer(data=request.data,
                                            context={'thread_id':thread_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
