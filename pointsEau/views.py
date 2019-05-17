from django.shortcuts import render, redirect
from .forms import EditPointEauForm, PointEauForm
from .models import PointEau
from rest_framework import generics
from pointsEau.models import PointEau
from .api.serializers import PointEauSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
import EnCasDeSoif.views as ecv
from django.contrib import messages as msg


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
                npe = serializer.save(owner=request.user)
                msg.success(request, "Le point a été ajouté !")
                return redirect('index')
    else:
        form = PointEauForm()

    return render(request, 'pointsEau/newPE.html', {'form': form, 'active': 'pointseau'})


def viewPE(request):
    user = request.user
    ownerPeau = user.pointseau.all()
    return render(request, 'pointsEau/viewPE.html', {'pointseau': ownerPeau, 'active': 'pointseau'})


def editPE(request, pk):
    user = request.user
    pe = PointEau.objects.get(pk=pk)
    # Si on essaye d'éditer un point d'eau pas à lui
    if pe.owner.id != request.user.id:
        # TODO: gérer l'erreur autrement
        raise("Erreur : this is not your point d'eau !!")

    if request.method == 'POST':
        form = PointEauForm(request.POST, instance=pe)
        if form.is_valid():
            form.save()
            return redirect('/pointsEau/lister')
    else:
        form = PointEauForm(instance=pe)

    return render(request, 'pointsEau/editPE.html', {'form': form, 'active': 'pointseau'})


def init(request):
    try:
        sampleUser = User.objects.get(username='sampleUser')
    except BaseException:
        sampleUser = User.objects.create_user(username='sampleUser', email='sample.user@sampleMail.com', password='samplePassword')
        
    PointEau.objects.create(nom="Point eau 1", lat=43.09, long=34.00, desc="Point eau 1", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 2", lat=12.09, long=54.099, desc="Point eau 2", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 3", lat=34.00, long=22.009, desc="Point eau 3", owner=sampleUser)
    return HttpResponse("Done !")
