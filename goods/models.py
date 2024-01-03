from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(
        verbose_name="Название категории", max_length=50, unique=True, db_index=True
    )
    slug = models.SlugField(verbose_name="Слаг категории", max_length=50, unique=True)
    z_index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер", blank=True, null=True
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ("z_index",)

    def __str__(self):
        return self.name


def product_image_upload_to(instance, filename):
    return f"product_images/{instance.name}/{filename}"


class Products(models.Model):
    category = models.ForeignKey(
        verbose_name="Категория продукта",
        to=Categories,
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(
        verbose_name="Название продукта", max_length=50, unique=True, db_index=True
    )
    slug = models.SlugField(
        verbose_name="Слаг продукта", max_length=50, unique=True, null=True
    )
    z_index = models.PositiveSmallIntegerField(
        verbose_name="Порядковый номер", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        verbose_name="Изображение",
        blank=True,
        null=True,
        upload_to=product_image_upload_to,
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=6,
        decimal_places=2,
        default=0.00,
        blank=True,
        null=True,
    )
    discount = models.DecimalField(
        verbose_name="Скидка %",
        max_digits=6,
        decimal_places=2,
        default=0.00,
        blank=True,
        null=True,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name="Количество", default=0, blank=True, null=True
    )
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    # todo: Довести до ума логику авто заполнения времени
    created_at = models.DateTimeField(
        verbose_name="Время создания", auto_now_add=True, blank=True, null=True
    )
    # todo: Сделать автоматическое присваевание создателя к объекту
    created_by = models.ForeignKey(
        verbose_name="Создатель",
        on_delete=models.CASCADE,
        related_name="created_categories",
        to=User,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("z_index",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("goods:product_page", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.pk:05}"

    def sell_price(self):
        if self.discount:
            discount_price = round(self.price - self.price * self.discount / 100, 2)
            return discount_price
        return self.price
