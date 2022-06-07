from django.urls import path, include

from .api import urlpatterns as api_urls
from .views import RegionCountryView

urlpatterns = [
    path('<int:country>/country-region/', RegionCountryView.as_view(), name='region_country'),
    path('shrine/', include('shrine.urls')),
]

urlpatterns += api_urls
