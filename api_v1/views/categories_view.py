from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import goods_serializers
from goods import models


@extend_schema_view(
    list=extend_schema(summary="Список категорий", tags=["Категории"]),
    retrieve=extend_schema(summary="Деталка категории", tags=["Категории"]),
    create=extend_schema(summary="Создать категорию", tags=["Категории"]),
    update=extend_schema(summary="Изменить категорию", tags=["Категории"]),
    destroy=extend_schema(summary="Удалить категорию", tags=["Категории"]),
    partial_update=extend_schema(
        summary="Изменить категорию частично", tags=["Категории"]
    ),
)
class CategoryAPIView(ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = goods_serializers.CategorySerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    # pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "z_index"]
    search_fields = ["name", "id"]
