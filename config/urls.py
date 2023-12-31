from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api_v1.urls", namespace="api_v1")),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="goods")),
    path("user/", include("users.urls", namespace="users")),
    path("cart/", include("carts.urls", namespace="carts")),
    path("orders/", include("orders.urls", namespace="orders")),
    # documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
