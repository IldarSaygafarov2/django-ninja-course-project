from ninja import NinjaAPI

from core.api.routes import api_router

api = NinjaAPI()

api.add_router('/api/', api_router)
