from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shrine
from .serializers import ShrineSerializer


class ShrineViewSet(ModelViewSet):
    queryset = Shrine.objects.all()
    serializer_class = ShrineSerializer



