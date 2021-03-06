from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название")

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product",
        verbose_name="Продавец"
    )

    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_images",
        verbose_name="Изображение товара",
        default="static/no_image.phg"
    )

    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")

    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="Цена")

    sales = models.IntegerField(
        default=0,
        verbose_name="Продано")

    available = models.BooleanField(
        default=True,
        verbose_name="В наличии")

    deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товар"
