from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Shrine
from .serializers import ShrineSerializer
from rest_framework.generics import ListAPIView


class ShrineViewSet(ModelViewSet):
    queryset = Shrine.objects.all()
    serializer_class = ShrineSerializer


class ShrineRegionsView(ListAPIView):
    queryset = Shrine.objects.all()
    serializer_class = ShrineSerializer

    def list(self, request, *args, **kwargs):
        region = kwargs.get('region', 1)
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(region=region)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

