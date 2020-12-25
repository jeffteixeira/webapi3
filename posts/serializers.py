from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'body',
            'profile'
        )


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'body',
            'profile',
            'comments'
        )