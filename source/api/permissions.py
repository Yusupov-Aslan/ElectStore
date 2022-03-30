from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_staff):
            return True
        return False


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user and request.user.is_staff:
            return True
        elif request.method == "POST":
            return True
        return False


class IsCartItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False

