from django.db import models
from django.template.defaultfilters import slugify

from core.apps.base_app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Короткая ссылка', unique=True)
    icon = models.FileField(verbose_name='Иконка', upload_to='categories/icons/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Subcategory(BaseModel):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='Короткая ссылка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['-created_at']
