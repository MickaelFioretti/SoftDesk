from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "name",
            "description",
            "status",
            "priority",
            "tag",
            "project",
            "assigned_to",
            "created_time",
            "owner",
        ]
