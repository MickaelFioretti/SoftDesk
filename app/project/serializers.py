from rest_framework import serializers
from .models import Project, Contributor


# ---- Contributors ----
class ContributorGetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    project = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = [
            "id",
            "user",
            "project",
        ]


class ContributorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "id",
            "user",
            "project",
        ]


# ---- Projects ----


class ProjectSerializer(serializers.ModelSerializer):
    contributors = ContributorGetSerializer(many=True, read_only=True)

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
