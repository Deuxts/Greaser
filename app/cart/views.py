from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart


# login_required sirve para obligar al usuario a entrar a su sesión
@login_required(login_url='/autenticacion/acceder')
def add_product(request, product_id): # agrega productos
    cart = Cart(request)    # actualiza
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("listado_productos")


@login_required(login_url='/autenticacion/acceder')
def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("listado_productos")


@login_required(login_url='/autenticacion/acceder')
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("listado_productos")


@login_required(login_url='/autenticacion/acceder')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listado_productos")