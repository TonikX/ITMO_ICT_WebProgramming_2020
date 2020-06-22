from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.user.is_superuser)
