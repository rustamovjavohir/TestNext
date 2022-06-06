from .views import (ShrineViewSet)
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register(f'shrine', ShrineViewSet, basename='shrine')

urlpatterns = routers.urls
