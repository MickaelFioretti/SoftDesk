# permissions.py

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Vous n'avez pas la permission de modifier ce commentaire."

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsProjectContributor(permissions.BasePermission):
    message = "Vous devez être contributeur de ce projet."

    def has_object_permission(self, request, view, obj):
        return obj.contributors.filter(user=request.user).exists()
