from rest_framework import routers
from .views import PointEauViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pointseau', PointEauViewSet, base_name='pointseau')
urlpatterns = router.urls