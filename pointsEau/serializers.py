from .models import PointEau
from rest_framework import serializers

class PointEauSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointEau
        fields = '__all__' 
        