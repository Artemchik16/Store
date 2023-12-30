from django.urls import path

from goods import views

app_name = "goods"

# namespace 'goods'

urlpatterns = [
    path("", views.CatalogPage.as_view(), name="catalog_page"),
    path("<slug:category_slug>/", views.CatalogPage.as_view(), name="catalog_page"),
    path("product/<slug:product_slug>/", views.ProductPage.as_view(), name="product_page"),
]
