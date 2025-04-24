from ninja import Schema
from core.api.schemas.categories.schema import CategorySchema
from decimal import Decimal
from typing import Optional


class ProductListItemSchema(Schema):
    id: int
    name: str
    slug: str
    price: Decimal
    preview: Optional[str]
    category: CategorySchema


class ProductDetailSchema(Schema):
    pass


class ProductColorSchema(Schema):
    pass


class ProductGallerySchema(Schema):
    pass


class ProductSizeSchema(Schema):
    pass


class ProductCharacteristicsSchema(Schema):
    pass
