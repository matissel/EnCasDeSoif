from django.urls import path, include
from .views import addPE, init, editPE
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('nouveau/', addPE, name="newPE"),
    path('editer/', editPE, name="editPE"),
    path('init', init, name="init")
]
