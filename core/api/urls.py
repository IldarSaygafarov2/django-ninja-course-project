from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI
from core.api.routes import api_router
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)
api.add_router("/api/", api_router)
