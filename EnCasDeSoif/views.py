from django.shortcuts import redirect
from pointsEau.models import PointEau
from django.shortcuts import render, redirect
import requests


def login_redirect(request):
    return redirect('/account/login')


def index(request):
    existingPoints = PointEau.objects.all()
    mapbox_access_token = "pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w"
    url = "http://localhost:8000/api/all"
    toutLesPoints = requests.get(url=url).json()

    geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

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
        geojson['features'].append(nouveauPoint)

    args = {
        'mapbox_access_token': mapbox_access_token,
        'allpe': geojson
    }
    return render(request, 'index.html', args)
