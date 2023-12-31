from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
        )

    def validate_age(self, value):
        if value is None or value < 15:
            raise serializers.ValidationError("L'âge minimum requis est de 15 ans.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            age=validated_data["age"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
