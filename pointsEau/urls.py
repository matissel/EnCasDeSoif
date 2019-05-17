from django.urls import path, include
from .views import addPE, init, editPE, viewPE
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('nouveau/', addPE, name="newPE"),
    path('lister', viewPE, name="listPE"),
    path('editer/<int:pk>', editPE, name="editPE"),
    path('init', init, name="init")
]
