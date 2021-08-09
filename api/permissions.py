from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnUserProfile(BasePermission):
    """Allow user to edit their own user profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own user profile"""
        if request.method in SAFE_METHODS:
            return True

        return request.user.id == obj.id


class SuperUserOnly(BasePermission):
    """Allow only superuser to edit model objects"""

    def has_object_permission(self, request, view, obj):
        """Check if user is superuser"""
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser