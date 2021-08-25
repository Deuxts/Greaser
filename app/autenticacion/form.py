from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

# solo tenemos un formulario el cual servirá para el registro del usuario (el registro de nuevos productos se hace
# desde la administración) el formulario presente, en realidad reescribe el predeterminado (como si hiciéramos una
# sobrecarga de métodos, para poder agregar más campos.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "date_joined", "email", "password1", "password2"]
