from django.urls import path
from .views import listado_productos,carrito_cel

urlpatterns = [
    path('', listado_productos, name='listado_productos'),
    path('carrito_cel/', carrito_cel, name='carrito_cel')
]
