from .serializers import PointEauSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from pointsEau.models import PointEau
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .permissions import IsGetOrIsAuthenticated

class PointEauViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer,)
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer
    permission_classes = [IsGetOrIsAuthenticated, ]

class PointsEauList(APIView):
    def get(self, request, format=None):
        snippets = PointEau.objects.all()
        serializer = PointEauSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PointEauSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PointsEauDetail(APIView):
    def get_object(self, pk):
        try:
            return PointEau.objects.get(pk=pk)
        except PointEau.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PointEauSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PointEauSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)