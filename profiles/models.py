from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    