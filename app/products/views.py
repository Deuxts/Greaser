from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.cart import Cart
from django.core.paginator import Paginator
# Create your views here.


def listado_productos(request):
    cart = Cart(request)
    listado_product = Product.objects.all()
    paginator = Paginator(listado_product, 6)
    pagina = request.GET.get("page") or 1
    products = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, products.paginator.num_pages + 1)
    return render(request, "products/listado.html", {
        "products": products, "paginas": paginas, "pagina_actual": pagina_actual
    })


def carrito_cel(request):
    cart = Cart(request)
    listado_product = Product.objects.all()
    paginator = Paginator(listado_product, 6)
    pagina = request.GET.get("page") or 1
    products = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, products.paginator.num_pages + 1)
    return render(request, "cart/cel_cart.html", {
        "products": products, "paginas": paginas, "pagina_actual": pagina_actual
    })
