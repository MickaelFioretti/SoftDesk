from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue


class Comment(models.Model):
    text = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
