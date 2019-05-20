from django.shortcuts import redirect
from pointsEau.models import PointEau
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from pointsEau.pointEau_api import afficherToutPoints
from pointsEau.models import PointEau
import json
from django.contrib import messages as msg
from pointsEau.api.tokenHandler import getTemporaryToken

def login_redirect(request):
    return redirect('/account/login')


def about(request):
    return render(request, 'about.html', {'active': 'about'})


def index(request, messages=[]):
    existingPoints = PointEau.objects.all()
    toutLesPoints = json.loads(afficherToutPoints(request).content)
    mapboxToken = getTemporaryToken

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
        'mapboxToken' : mapboxToken,
        'allpe': geojson,
        'lurl': request.build_absolute_uri,
        'active': 'index'
    }
    
    return render(request, 'index.html', args)
