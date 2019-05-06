from django.shortcuts import render,redirect
from .forms import PointEauForm
from rest_framework import generics 
from .serializers import PointEauSerializer
from .models import PointEau

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


class ListPointEauView(generics.ListAPIView):
    queryset = PointEau.objects.all()
    serializer_class = PointEauSerializer