from django.urls import path
from .views import *

app_name = "cart"

# estas urls llaman a funciones para actualizar el carrito
urlpatterns = [
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
    path('clear/', clear_cart, name='clear_cart'),
]
