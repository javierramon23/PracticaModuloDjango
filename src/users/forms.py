from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario de ALTA de un nuevo Usuario:
class SignupForm(UserCreationForm):

    class Meta:
        # Modelo a partir del que se genera el formulario.
        model = User
        # Campos que se muestran en el formulario.
        fields = ['username', 'first_name', 'last_name', 'email']

# Formulario de LOGIN de acceso:
class LoginForm(forms.Form):

    # Campos que componen el formulario.
    username = forms.CharField(label='Username:')
    password = forms.CharField(widget=forms.PasswordInput, label='Password:')
