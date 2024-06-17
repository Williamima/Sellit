from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminOrSafe(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_superuser
        )


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
