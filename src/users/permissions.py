# Se IMPORTAN los componentes necesarios.
from rest_framework.permissions import BasePermission

# CLASE que DEFINE los PERMISOS necesarios para utilizar los END POINT's
class UserPermissions(BasePermission):

    # El METODO 'has_permission()' determina
    def has_permission(self, request, view):

        # Cualquiera puede CREAR un USUARIO.
        # Para el resto de ACCIONES se tiene que se Usuario REGISTRADO o ADMINISTRADOR.
        if request.method == 'POST' or request.user.is_superuser or request.user.is_authenticated:
            return True
        #if request.user.is_authenticated:
            #return True

    # El METODO 'has_object_permission()' determina
    def has_object_permission(self, request, view, obj):

        # Las ACCIONES sóbre un OBJETO CONCRETO sólo las puede hacer el ADMINISTADOR
        # o el PROPIETARIO del OBJETO.
        if request.user == obj or request.user.is_superuser:
            return True
