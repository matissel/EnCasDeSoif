from django.shortcuts import render,redirect
from .forms import PointEauForm
from rest_framework import generics 
from .serializers import PointEauSerializer
from .models import PointEau
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def addPE(request):
    if request.method == 'POST':
        form = PointEauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('newPE')
    else:
        form = PointEauForm()
        args = {'form': form}
    return render(request, 'pointsEau/newPE.html', args)


class ListPointEauView(APIView):
    #queryset = PointEau.objects.all()
    #serializer_class = PointEauSerializer
    def get(self,request):
        allpe = PointEau.objects.all()
        serializer = PointEauSerializer(allpe, many=True)
        return Response({"allpe":serializer.data})
    

def afficherPointsEau(request):
    allpe = PointEau.objects.all()
    serializer = PointEauSerializer(allpe, many=True)

    args = {
        'points' : serializer.data,
    }

    return render(request, 'pointsEau/testmap.html',  args)