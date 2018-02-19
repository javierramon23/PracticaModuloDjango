# Se IMPORTAN los componentes necesarios.
from rest_framework.permissions import BasePermission

# CLASE que DEFINE los PERMISOS necesarios para utilizar los END POINT's
class UserPermissions(BasePermission):

    # El METODO 'has_permission()' determina
    def has_permission(self, request, view):

        if request.method == 'POST' or request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            return True

    # El METODO 'has_object_permission()' determina
    def has_object_permission(self, request, view, obj):

        if request.user == obj or request.user.is_superuser:
            return True
