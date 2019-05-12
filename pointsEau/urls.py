from django.urls import path, include
from .views import addPE
from .pointEau_api import afficherToutPoints

urlpatterns = [
    path('nouveau/', addPE, name="newPE"),
]