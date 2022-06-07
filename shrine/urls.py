from django.urls import path

from .api import urlpatterns as api_urls
from .views import ShrineRegionsView

urlpatterns = [
    path('<int:region>/shrines/', ShrineRegionsView.as_view(), name='shrines_region')
]

urlpatterns += api_urls
