from rest_framework import serializers
from models import Thread, Post


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'posts')
        read_only_fields = ('id', 'posts')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
