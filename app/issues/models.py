from django.db import models
from django.conf import settings
from project.models import Project


class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("FINISHED", "Finished"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    PRIORITY_CHOICES = [("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High")]
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="MEDIUM"
    )
    TAG_CHOICES = [("BUG", "Bug"), ("FEATURE", "Feature"), ("TASK", "Task")]
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues"
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_issues",
    )
