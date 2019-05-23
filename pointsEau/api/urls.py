from rest_framework import routers
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'pointseau', views.PointEauViewSet)
router.register(r'users', views.UserViewSet)

# API URLs determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
