from rest_framework import serializers
from .models import Shrine


class ShrineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shrine
        fields = '__all__'

