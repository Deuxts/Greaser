def cart_total_amount(request):
    total = 0.0
    if request.user.is_authenticated:  # verifica que el usuario esté ingresado a la pagina
        for key, value in request.session['cart'].items():  # verifica la sesion para que busque el carro del usuario
            total = total + (float(value['price']) * value['quantity'])
    return {'cart_total_amount': total}
