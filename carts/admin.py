from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "created_timestamp", "user_display"]
    readonly_fields = ["product", "quantity", "user_display"]
    list_filter = ["product__category__name", "created_timestamp"]
    search_fields = ["product__category__name", "product__name"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'

    user_display.short_description = "Имя пользователя"


class CartTabularAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 2
