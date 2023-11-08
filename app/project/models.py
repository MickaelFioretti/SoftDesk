from django.db import models
from django.conf import settings


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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_projects",
    )

    def __str__(self):
        return self.name


# Modèle pour les contributeurs
class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="contributors", null=True
    )
