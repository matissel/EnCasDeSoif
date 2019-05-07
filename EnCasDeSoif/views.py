from django.shortcuts import redirect
from pointsEau.models import PointEau
from django.shortcuts import render, redirect


def login_redirect(request):
    return redirect('/account/login')


def index(request):
    existingPoints = PointEau.objects.all()
    mapbox_access_token = "pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w"
    args = {
        'mapbox_access_token': mapbox_access_token,
        'test': 'zizi'
    }
    return render(request, 'index.html', args)
