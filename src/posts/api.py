from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from posts.permissions import BlogPermission
from posts.serializers import UserSerializer

# VIEW que muestra un LISTADO de los Blogs que contine la plataforma
class BlogListAPI(ListAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = [BlogPermission]
