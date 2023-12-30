# Generated by Django 4.2 on 2023-12-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0003_alter_products_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="slug",
            field=models.SlugField(
                blank=True, null=True, unique=True, verbose_name="Слаг продукта"
            ),
        ),
    ]