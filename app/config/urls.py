from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Estas Urls son especiales, pues en realidad están “heredando” las
# distintas urls que contienen los otros módulos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include("autenticacion.urls")),
    path('product/', include("products.urls")),
    path('', include("products.urls")),
    path('cart/', include("cart.urls")),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
