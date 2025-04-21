
from django.contrib import admin
from django.urls import path
from core.api.urls import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls)
]
