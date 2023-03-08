from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """Проверка соответствия автора поста и текущего юзера."""
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
