from django.shortcuts import render, redirect
from .forms import PointEauForm
from .models import PointEau
from rest_framework import generics 
from pointsEau.models import PointEau
from .api.serializers import PointEauSerializer


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

