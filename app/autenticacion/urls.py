from django.urls import path
from .views import *


# Estas Urls son las da el nombre e identifican su orden en la barra del navegador

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir"),
]
