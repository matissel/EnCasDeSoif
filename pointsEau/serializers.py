from .models import PointEau
from rest_framework import serializers


class PointEauSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    long = serializers.DecimalField(max_digits=10, decimal_places=8)
    lat = serializers.DecimalField(max_digits=10, decimal_places=2)
    desc = serializers.CharField(max_length=255)
