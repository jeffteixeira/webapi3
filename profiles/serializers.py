from rest_framework import serializers
from .models import Profile
from posts.serializers import PostSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'url',
            'name',
            'email'
        )

class ProfilePostSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = Profile
        fields = (
            'url',
            'name',
            'email',
            'posts'
        )