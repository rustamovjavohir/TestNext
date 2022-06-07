from django.urls import path, include

from .api import urlpatterns as api_urls
from .views import CountryView


urlpatterns = [
    path('c/', CountryView.as_view(), name='country_list'),
    path('region/', include('region.urls')),
]

urlpatterns += api_urls
