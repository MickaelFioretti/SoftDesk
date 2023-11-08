from rest_framework import serializers
from .models import Project, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # project = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = [
            "id",
            "user",
            "project",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField()
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


# TODO: Add serializer for post and get requests
