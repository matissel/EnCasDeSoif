from .serializers import PointEauSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from pointsEau.models import PointEau
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly


class PointEauViewSet(viewsets.ModelViewSet):
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer