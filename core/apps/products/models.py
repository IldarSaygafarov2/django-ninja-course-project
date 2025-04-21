from django.db import models

from core.apps.categories.models import Category
from core.apps.base_app.models import BaseModel




class Product(BaseModel):
    name = ''
    slug = ''
    price = ''
    description = ''
    quantity = ''


class ProductColor(models.Model):
    pass


class ProductGallery(models.Model):
    pass


class ProductCharacteristics(models.Model):
    pass


class ProductSize(models.Model):
    pass



