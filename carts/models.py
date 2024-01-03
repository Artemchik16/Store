from django.contrib.auth import get_user_model
from django.db import models

from goods.models import Products

User = get_user_model()


class CartQueryset(models.QuerySet):
    def total_price(self):
        if self:
            return sum(cart.product_price() for cart in self)
        return 0

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )

    class Meta:
        db_table = "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("created_timestamp",)

    objects = CartQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f"{self.user.username} | {self.product.name} | {self.quantity} шт"
        return f"Анонимный пользователь | {self.product.name} | {self.quantity} шт"

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
