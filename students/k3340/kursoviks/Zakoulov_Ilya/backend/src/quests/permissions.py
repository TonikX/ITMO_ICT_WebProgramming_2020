from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsAdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super().has_permission(request, view)
