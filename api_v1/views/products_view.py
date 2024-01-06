from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import goods_serializers
from goods import models


@extend_schema_view(
    list=extend_schema(summary="Список товаров", tags=["Продукты"]),
    retrieve=extend_schema(summary="Деталка товара", tags=["Продукты"]),
    create=extend_schema(summary="Создать товар", tags=["Продукты"]),
    update=extend_schema(summary="Изменить товар", tags=["Продукты"]),
    destroy=extend_schema(summary="Удалить товар", tags=["Продукты"]),
    partial_update=extend_schema(
        summary="Изменить товар частично", tags=["Продукты"]
    ),
)
class ProductsAPIView(ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = goods_serializers.ProductSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    # pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "z_index"]
    search_fields = ["name", "id"]
