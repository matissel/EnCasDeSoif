from .serializers import PointEauSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from pointsEau.models import PointEau
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsGetOrIsAuthenticated

class PointEauViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer,)
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
    permission_classes = [IsGetOrIsAuthenticated, ]

@api_view(['GET', 'POST'])
def points_eau_list(request):
    if request.method == 'GET':
        list_pe = PointEau.objects.all()
        serializer = PointEauSerializer(list_pe, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PointEauSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def points_eau_detail(request, pk):
    try:
        pe = PointEau.objects.get(pk=pk)
    except PointEau.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PointEauSerializer(pe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PointEauSerializer(pe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)