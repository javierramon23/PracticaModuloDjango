# Se IMPORTAN los componentes necesarios.
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from users.permissions import UserPermissions
from users.serializers import UserSerializer, UserDetailSerializer, UserListSerializer
from rest_framework import filters

# VIEW que permite la creacion de un Usuario.
class UserAddAPI(CreateAPIView):

    # QUERYSET sobre la BD ¿¿¿NECESARIO para la CREACION???
    queryset = User.objects.all()
    # SERIALIZER que se utiliza para el tratamiento de la SOLICITUD y RESPUESTA.
    serializer_class = UserSerializer
    # Conjnto de PERMISOS.
    permission_classes = [UserPermissions]


# VIEW que permite el DETALLE, la ACTUALIZACION y el BORRADO de un Usuario.
class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    # QUERYSET sobre la BD. ¿¿¿ Y la PK ???
    queryset = User.objects.all()

    # Conjunto de PERMISOS.
    permission_classes = [UserPermissions]

    # SERIALIZER que se utiliza para el tratamiento de la SOLICITUD y RESPUESTA.
    # En función del METODO de la SOLICITUD se establece uno u otro.
    def get_serializer_class(self):
        return UserDetailSerializer if self.request.method == 'GET' else UserSerializer

    """
    NOTA:
    A la hora de BORRAR, ¿QUE PASA CON LOS POST DEL USUARIO?
    """


# VIEW que permite LISTAR los Usuarios del sitema, es decir, los BLOGS.
class UserListAPI(ListAPIView):
    # CONSULTA sobre la BD.
    queryset = User.objects.all()
    # SERIALIZER que se va a utilizar para el tratamiento de la SOLICITUD y RESPUESTA.
    serializer_class = UserListSerializer

    # Se definene los FILTROS por los que se va a poder realizar la CONSULTA
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    # Y los CAMPOS por los que se realizará la BUSQUEDA y la ORDENACION.
    search_fields = ('username',)
    ordering_fields = ('username',)

    # En este caso NO se define ningun conjunto de PERMISOS
    # por que esta acción la puede realizar CUALQUIER Usuario.



