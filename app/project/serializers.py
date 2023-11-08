from rest_framework import serializers
from .models import Project, Contributor
from authentication.serializers import UserSerializer


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = [
            "id",
            "user",
            "project",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "project_type",
            "owner",
            "contributors",
        ]
