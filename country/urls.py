from django.urls import path

from .api import urlpatterns as api_urls
from .views import CountryView


urlpatterns = [
    path('c/', CountryView.as_view(), name='country_list'),
]

urlpatterns += api_urls
