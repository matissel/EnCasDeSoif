from pointsEau.models import PointEau
from rest_framework import serializers


class PointEauSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointEau
        fields = [
            'pk',
            'nom',
            'lat',
            'long',
            'desc',
            'owner'
        ]
    nom = serializers.CharField(max_length=100)
    long = serializers.DecimalField(max_digits=10, decimal_places=8)
    lat = serializers.DecimalField(max_digits=10, decimal_places=8)
    desc = serializers.CharField(max_length=255)
