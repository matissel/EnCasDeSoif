from django.shortcuts import render, redirect
from .forms import PointEauForm
from .models import PointEau
from rest_framework import generics
from pointsEau.models import PointEau
from .api.serializers import PointEauSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse


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

    return render(request, 'pointsEau/newPE.html', {'form': form, 'active': 'newPE'})


def init(request):
    try:
        sampleUser = User.objects.get(username='sampleUser')
    except BaseException:
        sampleUser = User.objects.create_user(username='sampleUser', email='sample.user@sampleMail.com', password='samplePassword')

    PointEau.objects.create(nom="Point eau 1", lat=43.09, long=34.00, desc="Point eau 1", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 2", lat=12.09, long=54.099, desc="Point eau 2", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 3", lat=34.00, long=22.009, desc="Point eau 3", owner=sampleUser)
    return HttpResponse("Done !")
