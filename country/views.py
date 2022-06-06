from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .models import Country
from .serializers import CountrySerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    # def list(self, request, *args, **kwargs):


class CountryView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



