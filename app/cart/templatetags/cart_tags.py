from django import template

register = template.Library()


# sirve para multiplicar los precios del carro
@register.filter()
def multiply(value, arg):
    return float(value) * arg


# sirve para darle formato a la moneda
@register.filter()
def money_format(value, arg):
    return  f"{value}{arg}"