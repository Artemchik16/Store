from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import goods_serializers
from goods import models


class CategoryAPIView(ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = goods_serializers.CategorySerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "z_index"]
    search_fields = ["name", "id"]
