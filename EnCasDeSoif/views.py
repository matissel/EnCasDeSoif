from django.shortcuts import redirect
from pointsEau.models import PointEau
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from pointsEau.pointEau_api import afficherToutPoints
from pointsEau.models import PointEau

import json


def login_redirect(request):
    return redirect('/account/login')


def index(request):
    existingPoints = PointEau.objects.all()
    # TODO : sécuriser la clé de l'API
    mapbox_access_token = "pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w"
    toutLesPoints = json.loads(afficherToutPoints(request).content)

    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

    # Parcours de tous les points recus par la requete pour la vue
    for point in toutLesPoints['allpe']:

        nouveauPoint = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [point['long'], point['lat']]
            },
            'properties': {
                'title': point['nom'],
                'description': point['desc']
            }
        }
        # Ajout a un objet JSON pour la vue
        geojson['features'].append(nouveauPoint)

    args = {
        'mapbox_access_token': mapbox_access_token,
        'allpe': geojson,
        'lurl': request.build_absolute_uri
    }
    return render(request, 'index.html', args)

def init(request):
    sampleUser = User.objects.get(username='sampleUser')
    if (sampleUser == None):
        sampleUser = User.objects.create_user(username='sampleUser', email='sample.user@sampleMail.com', password='samplePassword')

    PointEau.objects.create(nom="Point eau 1", lat=43.09, long=34.00, desc="Point eau 1", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 2", lat=12.09, long=54.099, desc="Point eau 2", owner=sampleUser)
    PointEau.objects.create(nom="Point eau 3", lat=34.00, long=22.009, desc="Point eau 3", owner=sampleUser)
    return HttpResponse("Done !")