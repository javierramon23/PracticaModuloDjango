# Se IMPORTAN los componentes necesarios.
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

# SERIALIZER para tratar el FORMATO de la SOLICITUD y LA RESPUESTA.
class UserSerializer(serializers.ModelSerializer):

    # Se SOBREESCRIBE los siguientes ATRIBUTOS para que sean OBLIGATORIOS.
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        # MODELO en el que se basa el SERIALIZER.
        model = User
        # CAMPOS del MODELO que se MUESTRAN y se REQUIEREN
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

    # VALIDATOR para el ATRIBUTO 'password' del MODELO
    # Se encarga de realizar el HASHEADO de la password.
    def validate_password(self, value):
        # El METODO make_password() genera el HASH del PARAMETRO que se le pasa.
        return make_password(value)


# SERIALIZER para tratar el FORMATO de la SOLICITUD y LA RESPUESTA.
class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        # MODELO en el que se basa el SERIALIZER.
        model = User
        # CAMPOS del MODELO que se EXCLUIRAN.
        exclude = ['password']


# SERIALIZER para tratar el FORMATO de la SOLICITUD y LA RESPUESTA.
class UserListSerializer(serializers.ModelSerializer):
    # Se define un CAMPO que almecenara la URL del BLOG
    # Se utiliza el METODO 'SerializerMethodField()' que recibe un METODO definido en el
    # SERIALIZER para calcular el valor del CAMPO.
    blog = serializers.SerializerMethodField('get_url_blog')

    class Meta:
        # MODELO que utiliza el SERIALIZER.
        model = User
        # CAMPOS del MODELO que se MOSTRARAN.
        # Mas el CAMPO PERSONALIZADO.
        fields = ['blog']

    # METODO que genera la URL del BLOG (Lo invocara 'SerializerMethodField')
    def get_url_blog(self, instance):
        # Se GUARDA la URL de DETALLE de un BLOG asociada a los DISTINTOS Usuarios.
        url = reverse_lazy('blog_detail_page', kwargs={'user_name': instance.username})
        # Se devuelve un string informando de la URL del Blog y a quien pertenece
        return 'El Blog de %s %s | URL: localhost:8000%s' % (instance.first_name, instance.last_name, url)


