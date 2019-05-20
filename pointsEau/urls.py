from django.urls import path, include
from .views import addPE, init, editPE, viewPE, delPE
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('nouveau/', addPE, name="newPE"),
    path('lister', viewPE, name="listPE"),
    path('editer/<int:pk>', editPE, name="editPE"),
    path('supprimer/<int:pk>', delPE, name="delPE"),
    path('init', init, name="init")
]
