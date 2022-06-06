from .views import (CountryViewSet)
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register(f'country', CountryViewSet, basename='country')

urlpatterns = routers.urls
