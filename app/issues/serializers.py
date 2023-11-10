from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
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
        ]
