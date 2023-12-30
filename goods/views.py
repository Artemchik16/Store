from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView

from goods import models as goods_models
from goods.utils import get_search_queryset


class CatalogPage(TemplateView):
    template_name = "goods/catalog.html"
    products_per_page = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = None

        try:
            if "category_slug" in self.kwargs:
                category_slug = self.kwargs["category_slug"]
                products = goods_models.Products.objects.filter(
                    category__slug=category_slug
                )
            else:
                products = goods_models.Products.objects.all()
        except Exception as ex:
            print(ex)

        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")

        search_query = self.request.GET.get("q")

        if search_query:
            products = get_search_queryset(search_query)
            print(search_query)

        if on_sale:
            products = products.filter(discount__gt=0)

        if order_by and order_by != "default":
            products = products.order_by(order_by)

        paginator = Paginator(products, self.products_per_page)
        page = int(self.request.GET.get("page", 1))

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context["products"] = products

        return context


class ProductPage(TemplateView):
    template_name = "goods/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            product_slug = self.kwargs["product_slug"]
            product = get_object_or_404(goods_models.Products, slug=product_slug)

            category = product.category
            total_products_in_category = goods_models.Products.objects.filter(
                category=category
            ).count()

            context["total_products_in_category"] = total_products_in_category
            context["product"] = product

            return context

        except Exception as ex:
            print(ex)
