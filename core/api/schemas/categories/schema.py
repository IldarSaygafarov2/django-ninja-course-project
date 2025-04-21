from datetime import datetime
from typing import Optional

from ninja import Schema


class SubcategorySchema(Schema):
    id: int
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime


class CategorySchema(Schema):
    id: int
    name: str
    slug: str
    icon: Optional[str]
    created_at: datetime
    updated_at: datetime
    subcategories: list[SubcategorySchema]