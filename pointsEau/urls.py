from django.urls import path, include
from .views import addPE, init
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('nouveau/', addPE, name="newPE"),
    path('init', init, name="init")
]
