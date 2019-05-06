from .models import PointEau
from rest_framework import serializers

class PointEauSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    long = serializers.IntegerField()   
    lat = serializers.IntegerField()     
    desc = serializers.CharField(max_length=255)
