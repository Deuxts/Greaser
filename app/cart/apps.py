from django.apps import AppConfig


# registro del nombre del módulo como app para poder llamarle en la configuración
class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
