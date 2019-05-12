from .serializers import PointEauSerializer
from rest_framework import viewsets
from pointsEau.models import PointEau
from pointsEau.forms import PointEauForm
from rest_framework.response import Response


class PointEauViewSet(viewsets.ModelViewSet):
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
