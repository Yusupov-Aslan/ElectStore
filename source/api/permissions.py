from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS or request.user.is_staff:
                return True
        return False
