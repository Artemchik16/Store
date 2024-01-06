from rest_framework import serializers

from goods import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ("name", "slug", "z_index")


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Products
        fields = (
            "id",
            "name",
            "slug",
            "category",
            "description",
            "sell_price",
            "price",
            "discount",
            "quantity",
            "is_active",
        )
