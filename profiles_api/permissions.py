from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Permite al usuario solo modificar su perfil"""

    def has_object_permission(self, request, view, obj):
        """Chequea si el usuario quiere modificar su perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
