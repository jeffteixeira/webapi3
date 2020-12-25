from django.db import models
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

