from .serializers import PointEauSerializer
from rest_framework import generics
from pointsEau.models import PointEau

class PointEauView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PointEauSerializer

    def get_queryset(self):
        return PointEau.objects.all()
