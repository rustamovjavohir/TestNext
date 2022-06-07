from .views import (RegionViewSet)
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register(f'region', RegionViewSet, basename='region')

urlpatterns = routers.urls
