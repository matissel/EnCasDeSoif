from django.urls import path, include
from .views import addPE, ListPointEauView

urlpatterns = [
    path('add/', addPE, name="newPE"),
    path('all/', ListPointEauView.as_view(), name="allpoints")
]