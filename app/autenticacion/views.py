from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from autenticacion.form import CustomUserCreationForm

# Aquí están declarada las funciones para la autenticación del login


def acceder(request):
    # Obtenemos el método post (esto se repite en varias funciones)
    if request.method == "POST":
        # obtenemos la información del formulario
        form = AuthenticationForm(request, data=request.POST)
        # validamos el los datos obtenidos, comparándolos con la base de datos
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenid@ de nuevo {nombre_usuario}")
                return redirect("listado_productos")
            # en caso contrario nos mostrará el mensaje de error
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    # retornamos la información al formulario
    form = AuthenticationForm()
    return render(request, "autenticacion/acceder.html", {"form": form})


# esta función crea la vista de la página web
class VistaRegistro(View):
    # comentario para que el IDE lo ignore
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        # Pasamos el formulario de “form.py”
        form = UserCreationForm()
        # retornamos al navegador las variables, junto con la plantilla de HTML que deberá mostrar
        return render(request, "autenticacion/registro.html", {"form": form})


def registro(request):
    # Pasamos el formulario de “form.py”
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        usuario = form.save()
        nombre_usuario = form.cleaned_data.get("username")
        messages.success(request, F"Bienvenid@ a la plataforma {nombre_usuario}")
        login(request, usuario)
        # lo Redireccionamos a la página del listado de productos
        return redirect("listado_productos")
    else:
        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])
            # retornamos al navegador las variables, junto con la plantilla de HTML que deberá mostrar y un error
        return render(request, "autenticacion/registro.html", {"form": form})


# Llama a la salida, de esta forma la sesión es terminada
def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")
