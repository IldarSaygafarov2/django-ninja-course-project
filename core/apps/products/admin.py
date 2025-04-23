from django.contrib import admin

from . import models


class ProductColorInline(admin.TabularInline):
    model = models.ProductColor
    extra = 1


class ProductGalleryInline(admin.TabularInline):
    model = models.ProductGallery
    extra = 1


class ProductCharacteristicsInline(admin.TabularInline):
    model = models.ProductCharacteristics
    extra = 1


class ProductSizeInline(admin.TabularInline):
    model = models.ProductSize
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductColorInline,
        ProductGalleryInline,
        ProductCharacteristicsInline,
        ProductSizeInline,
    ]
    prepopulated_fields = {"slug": ("name",)}
