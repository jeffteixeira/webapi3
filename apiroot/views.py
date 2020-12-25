from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from profiles.views import ProfileList
from posts.views import PostList, PostCommentList
from comments.views import CommentList


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'profiles': reverse(ProfileList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
            'post-comments': reverse(PostCommentList.name, request=request)
        })
