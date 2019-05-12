from .serializers import PointEauSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from pointsEau.models import PointEau
from pointsEau.forms import PointEauForm
from rest_framework.response import Response
from .permissions import IsGetOrIsAuthenticated
from rest_framework.permissions import IsAdminUser

class PointEauViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer,)
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
    permission_classes = [IsGetOrIsAuthenticated, ]

class AdminPointEauView(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer,)
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
    permission_classes = [IsAdminUser ]
