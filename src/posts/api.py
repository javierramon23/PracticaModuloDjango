from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostAddSerializer, PostListSerializer, PostDetailSerializer
from django.utils import timezone
from django.db.models import Q


class PostAddAPI(CreateAPIView):
    # QUERYSET sobre la BD ¿¿¿NECESARIO para la CREACION???
    queryset = Post.objects.all()
    # SERIALIZER que se utiliza para el tratamiento de la SOLICITUD y RESPUESTA.
    serializer_class = PostAddSerializer
    # Conjunto de PERMISOS.
    permission_classes = [PostPermission]

    # Se PERSONALIZA en comportamiento del METODO que CREA un POST
    def perform_create(self, serializer):
        # para ASIGNARLO al USUARIO que realiza la PETICION
        return serializer.save(owner=self.request.user)


class PostListAPI(ListAPIView):

    queryset = Post.objects.all()

    serializer_class = PostListSerializer

    permission_classes = [PostPermission]

    # Se definene los FILTROS por los que se va a poder realizar la CONSULTA
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    # Y los CAMPOS por los que se realizará la BUSQUEDA y la ORDENACION.
    search_fields = ('title', 'body')
    ordering_fields = ('title', 'publish_date')

    #
    lookup_url_kwarg = 'username'

    # Se MODIFICA la QUERYSET (CONSULTA a la BD) en función de una serie de CRITERIOS:
    def get_queryset(self):

        #
        username = self.kwargs.get(self.lookup_url_kwarg)

        #
        self.queryset = Post.objects.filter(owner__username=username).order_by('-publish_date')
        """
        
        """
        if not self.request.user.is_authenticated:
            return self.queryset.filter(publish_date__lte=timezone.now())

        if self.request.user.is_superuser:
            return self.queryset

        else:
            #return self.queryset.filter(owner=self.request.user)
            return self.queryset.filter(Q(owner=self.request.user) | Q(publish_date__lte=timezone.now()))


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()

    serializer_class = PostDetailSerializer

    permission_classes = [PostPermission]

    def get_queryset(self):

        if not self.request.user.is_authenticated:
            return self.queryset.filter(publish_date__lte=timezone.now())

        elif self.request.user.is_superuser:
            return self.queryset

        else:
            return self.queryset.filter(Q(owner=self.request.user) | Q(publish_date__lte=timezone.now()))
