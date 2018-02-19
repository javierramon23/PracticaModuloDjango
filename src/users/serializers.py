# Se IMPORTAN los componentes necesarios.
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

# SERIALIZER para tratar el FORMATO de la SOLICITUD y LA RESPUESTA.
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # MODELO en el que se basa el SERIALIZER.
        model = User
        # CAMPOS del MODELO que se MUESTRAN y se REQUIEREN
        fields = ['first_name', 'last_name', 'username', 'password', "email"]

    # VALIDATOR para el ATRIBUTO 'password' del MODELO
    # Se encarga de realizar el HASHEADO de la password.
    def validate_password(self, value):
        # El METODO make_password() genera el HASH del PARAMETRO que se le pasa.
        return make_password(value)
