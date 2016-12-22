from django.shortcuts import get_object_or_404
from rest_framework import serializers
from models import Thread, Post, Board


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'body', 'signature', 'topic', 'email', 'posted_at')
        read_only_fields = ('id', 'posted_at', 'thread_id')

    def create(self, validated_data):
        """
        Create and return a new `Board` instance, given the validated data.
        """
        if self.context.get('board') is not None:
            t = Thread()
            t.board = get_object_or_404(Board,
                                        short_name=self.context.get('board'))
            t.save()
            return Post.objects.create(thread=t, **validated_data)
        else:
            return Post.objects.create(thread=get_object_or_404(Thread,
                id=self.context.get('thread_id')), **validated_data)


class ThreadSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    def get_posts(self, thread):
        query = Post.objects.raw("(SELECT *\
            FROM board_post\
            WHERE thread_id = {thread_id}\
            ORDER BY id ASC LIMIT 1)\
            UNION\
            (SELECT * FROM board_post\
            WHERE thread_id = {thread_id}\
            ORDER BY id DESC LIMIT 3)".format(thread_id=thread))
        serializer = PostSerializer(query, many=True)
        return serializer.data

    class Meta:
        model = Thread
        fields = ('id', 'posts')
        read_only_fields = (('id',))
