from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
import json
from django.http import JsonResponse
from rest_framework import generics
from .serializers import PointEauSerializer
from .models import PointEau


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def afficherToutPoints(request, format=None):
    allpe = PointEau.objects.all()
    serializer = PointEauSerializer(allpe, many=True)
    args = {
        'allpe': serializer.data
    }
    return Response(args)

# points utilisateur

# post nouveau point

# modifier point eau

# supprimer point eau
