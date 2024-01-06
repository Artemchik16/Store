from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_v1.views import categories_view, products_view

app_name = "api_v1"

categories_router = DefaultRouter()
categories_router.register(r"categories", categories_view.CategoryAPIView)

products_router = DefaultRouter()
products_router.register(r"products", products_view.ProductsAPIView)

urlpatterns = [
    path("v1/", include(categories_router.urls)),
    path("v1/", include(products_router.urls)),
]
