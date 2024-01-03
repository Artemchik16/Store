from django.urls import path

from orders import views

app_name = "orders"

# namespace 'orders'

urlpatterns = [
    path("", views.create_order, name="order_page"),
]
