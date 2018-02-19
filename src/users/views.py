from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from users.forms import LoginForm, SignupForm


# CLASE que define los métodos para el REGISTRO de un NUEVO Usuario.
class SignupView(View):
    # Método que se ejecuta cuando la petición del Usuario sea de tipo GET.
    def get(self, request):
        # Se INSTANCIA un FORMULARIO
        form = SignupForm()
        # Se RENDERIZA la página con el FORMULARIO de ALTA.
        return render(request, 'signup_page.html', {'form': form})

    # Método que se ejecuta cuando la petición del Usuario sea de tipo POST.
    def post(self, request):
        # Se INSTANCIA un FORMULARIO con los DATOS que se han introducido.
        form = SignupForm(request.POST)

        # Si los datos son VALIDOS
        if form.is_valid():
            # Se GUARDAN el Usuario en la BD.
            form.save()
            # Se CREA un mensaje de EXITO para el Usuario.
            messages.success(request, 'El usuario ha sido dado de alta con exito.')
            # Se REDIRIGE al usuario a la página de LOGIN.
            return redirect('login_page')
        # Si los datos son INCORRECTOS
        else:
            # Se CREA un mensaje de ERROR para el Usuario
            messages.error(request, 'Revisa los datos del formulario!!!')
        # Se RENDERIZA la página de ALTA
        return render(request, 'signup_page.html', {'form': form})


# CLASE que define los métodos para el LOGIN de un Usuario.
class LoginView(View):

    # Método que se ejecuta cuando la petición del Usuario sea de tipo GET.
    def get(self, request):
        # Se INSTANCIA un FORMULARIO
        form = LoginForm()
        # Se RENDERIZA la página con el FORMULARIO de LOGIN.
        return render(request, 'login_page.html', {'form': form})

    # Método que se ejecuta cuando la petición del Usuario sea de tipo POST.
    def post(self, request):
        # Se INSTANCIA un FORMULARIO con los DATOS que se han introducido.
        form = LoginForm(request.POST)

        # Si los datos son VALIDOS
        if form.is_valid():

            # Se guardan los datos de ACCESO.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Se INSTANCIA un Usuario y se AUTENTICA.
            user = authenticate(username=username, password=password)

            # Si el Usuario EXISTE y esta ACTIVO
            if user and user.is_active:
                # Se LOGUEA en el sistema.
                login(request, user)
                # Se REDIRIGE al Usuario al HOME.
                return redirect('home_page')
            # Si no EXISTE o no esta ACTIVO
            else:
                # Se CREA un mensaje de ERROR para el Usuario.
                messages.error(request, 'El Usuario especificado no existe o está inactivo.')

        # Se RENDERIZA la página de LOGIN.
        return render(request, 'login_page.html', {'form': form})

# CLASE que define el método necesario para LOGOUT.
class LogoutView(View):

    # Método que se ejecuta cuando la petición del Usuario sea de tipo GET.
    def get(self, request):
        # Se hace el LOGOUT del Usuario.
        logout(request)
        # Se REDIRIGE al Usuario a la página de LOGIN.
        return redirect('login_page')
