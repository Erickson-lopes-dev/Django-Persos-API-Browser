from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Permissão apenas para o criador do Persos, e os demais apenas leitura
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
