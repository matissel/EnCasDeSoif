from django.shortcuts import render, redirect
from .forms import PointEauForm
from .models import PointEau
from rest_framework import generics
from pointsEau.models import PointEau
from .api.serializers import PointEauSerializer
from rest_framework import viewsets


def addPE(request):
    if request.method == 'POST':
        form = PointEauForm(request.POST)
        if form.is_valid():
            point = {
                'lat': form.cleaned_data['lat'],
                'long': form.cleaned_data['long'],
                'desc': form.cleaned_data['desc'],
                'owner': request.user.pk,
                'nom': form.cleaned_data['nom']
            }

            serializer = PointEauSerializer(data=point)
            if serializer.is_valid():
                npe = serializer.save()
                return redirect('index')

    else:
        form = PointEauForm()

    return render(request, 'pointsEau/newPE.html', {'form': form})
