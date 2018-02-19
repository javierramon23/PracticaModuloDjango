# Se IMPORTAN los componentes necesarios.
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from users.permissions import UserPermissions
from users.serializers import UserSerializer

# VIEW que permite la creacion de un Usuario.
class UserAddAPI(CreateAPIView):

    # QUERYSET sobre la BD ¿¿¿ NECESARIO???
    queryset = User.objects.all()
    # SERIALIZER que se utiliza para el tratamiento de la SOLICITUD y RESPUESTA.
    serializer_class = UserSerializer
    # Conjnto de PERMISOS.
    permission_classes = [UserPermissions]

# VIEW que permite el DETALLE, la ACTUALIZACION y el BORRADO de un Usuario.
class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    # QUERYSET sobre la BD. ¿¿¿ Y la PK ???
    queryset = User.objects.all()
    # SERIALIZER que se utiliza para el tratamiento de la SOLICITUD y RESPUESTA.
    serializer_class = UserSerializer
    # Conjnto de PERMISOS.
    permission_classes = [UserPermissions]


