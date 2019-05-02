from django.urls import path, include
from . import views

urlpatterns = [
    #path('', CARTE DES POINTS)
    path('add/', views.addPE, name="newPE"),
]