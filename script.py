from profiles.models import Profile
from posts.models import Post
from comments.models import Comment
import json


with open('db.json', 'r') as json_file:
    data = json.load(json_file)

users = data['users']
posts = data['posts']
comments = data['comments']

for user in users:
    Profile.objects.create(
        name=user['name'],
        email=user['email']
    )

for post in posts:
    profile = Profile.objects.get(id=post['userId'])
    Post.objects.create(
        title=post['title'],
        body=post['body'],
        profile=profile
    )

for comment in comments:
    post = Post.objects.get(id=comment['postId'])
    Comment.objects.create(
        name=comment['name'],
        email=comment['email'],
        body=comment['body'],
        post=post
    )
