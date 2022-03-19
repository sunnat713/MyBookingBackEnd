from rest_framework.permissions import BasePermission

class IsProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.id == obj.id or request.user.is_superuser)

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return (request.user.id == obj.user.id)

class IsRestaurantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return (request.user.id == obj.restaurant.user_id)