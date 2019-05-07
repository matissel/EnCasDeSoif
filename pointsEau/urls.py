from django.urls import path, include
from .views import addPE, ListPointEauView, afficherPointsEau

urlpatterns = [
    path('add/', addPE, name="newPE"),
    path('all/', ListPointEauView.as_view(), name="allpoints"),
    path('testmap/', afficherPointsEau, name='testmap')
]