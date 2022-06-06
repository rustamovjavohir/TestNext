from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Region
from .serializers import RegionSerializer


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


