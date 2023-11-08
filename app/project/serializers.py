from rest_framework import serializers
from .models import Project
from authentication.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "project_type",
            "owner",
        ]
        # Ajoutez tous les champs que vous voulez exposer via l'API.


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "projects",
        ]
        # Ajoutez tous les champs que vous voulez exposer via l'API.
