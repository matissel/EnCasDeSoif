from pointsEau.models import PointEau
from django.contrib.auth.models import User
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
    owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    pointseau = serializers.PrimaryKeyRelatedField(many=True, queryset=PointEau.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pointseau')