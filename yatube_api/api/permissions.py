"""Custom permission classes for API."""

from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Allow edits only for the object's author."""

    def has_object_permission(self, request, view, obj):
        """Return True for safe methods or object author."""
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
