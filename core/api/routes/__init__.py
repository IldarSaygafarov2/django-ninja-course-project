from ninja import Router

from .v1 import v1_router

api_router = Router()

api_router.add_router('/v1/', v1_router)
