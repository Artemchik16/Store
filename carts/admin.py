from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'created_timestamp', 'user']
    readonly_fields = ['product', 'quantity', 'user']
    list_filter = ['product__category__name']
    search_fields = ['product__category__name', 'product__name']
