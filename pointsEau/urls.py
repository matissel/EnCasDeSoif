from django.urls import path, include
from .views import addPE
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('add/', addPE, name="newPE"),
    path('all/', afficherToutPoints, name="allpoints"),
]