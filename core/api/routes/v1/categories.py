
from django.http import HttpRequest
from ninja import Router
from core.apps.categories.models import Category
from core.api.schemas.categories.schema import CategorySchema

router = Router(tags=['Categories'])


@router.get('/', response=list[CategorySchema])
def get_all_categories_data(request: HttpRequest):
    categories = Category.objects.all()
    return categories
