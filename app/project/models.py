from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    TYPE_CHOICES = [
        ("BE", "Back-End"),
        ("FE", "Front-End"),
        ("IOS", "iOS"),
        ("ANDROID", "Android"),
    ]
    project_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_projects"
    )


# Modèle pour les contributeurs
class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, related_name="contributors")
