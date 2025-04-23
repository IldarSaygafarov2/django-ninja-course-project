from django.db import models
from django.template.defaultfilters import slugify

from core.apps.categories.models import Category
from core.apps.base_app.models import BaseModel


class Product(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True)
    slug = models.SlugField(verbose_name="Короткая ссылка", unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(verbose_name="Кол-во товара", default=5)
    discount = models.PositiveSmallIntegerField(verbose_name="Размер скидки", default=0)
    preview = models.ImageField(
        verbose_name="Заставка",
        upload_to="products/previews/",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="category",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at"]


class ProductColor(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="colors",
    )
    color_name = models.CharField(
        verbose_name="Название цвета",
        unique=True,
        max_length=100,
    )
    color_code = models.CharField(verbose_name="Код цвета", max_length=12, unique=True)

    def __str__(self):
        return f"{self.product.name} - {self.color_name}"

    class Meta:
        verbose_name = "Цвет продукта"
        verbose_name_plural = "Цвета продукта"


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="gallery",
        verbose_name="Продукт",
    )
    photo = models.ImageField(verbose_name="Фото", upload_to="products/gallery/")

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продукта"


class ProductCharacteristics(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="characteristics",
    )
    key = models.CharField(verbose_name="Название характеристики", max_length=150)
    value = models.TextField(verbose_name="Значение характеристики")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Характеристика продукта"
        verbose_name_plural = "Характеристики продукта"


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="sizes",
    )
    length = models.IntegerField(default=0, verbose_name="Длина")
    width = models.IntegerField(default=0, verbose_name="Ширина")
    height = models.IntegerField(default=0, verbose_name="Высота")

    def __str__(self):
        return f"{self.length} СМ х {self.width} СМ х {self.height} СМ"

    class Meta:
        verbose_name = "Размер продукта"
        verbose_name_plural = "Размеры продукта"


# class ProductComment(BaseModel):
#     pass
