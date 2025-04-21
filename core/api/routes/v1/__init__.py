from ninja import Router

from .categories import router as categories_router


v1_router = Router()


v1_router.add_router('/categories/', categories_router)