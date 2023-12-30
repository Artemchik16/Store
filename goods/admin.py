from django.contrib import admin

from goods import models

admin.site.site_header = "By ShopyShop Admin"


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_product_counts", "slug", "z_index")
    search_fields = ("name", "slug")
    list_display_links = ("name", "id")
    list_editable = ("z_index",)
    search_help_text = "Введите название или слаг категории:"
    ordering = ("z_index",)
    prepopulated_fields = {"slug": ("name",)}

    def get_product_counts(self, obj):
        return obj.products.count()

    get_product_counts.short_description = "Количество связанных продуктов"


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "name",
        "slug",
        "z_index",
        "price",
        "discount",
        "quantity",
        "created_at",
        "created_by",
    )
    list_filter = ("category__name",)
    search_fields = ("name", "slug")
    list_display_links = (
        "name",
        "id",
    )
    list_editable = ("z_index", "quantity")
    ordering = ("z_index",)
    prepopulated_fields = {"slug": ("name",)}
